import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { runInNewContext } from 'node:vm';

const html = readFileSync(new URL('../web/index.html', import.meta.url), 'utf8');
const script = html.match(/<script>([\s\S]*?)<\/script>/)?.[1];
assert.ok(script, 'inline script should exist');

function element(extra = {}) {
  return {
    value: '', type: '', textContent: '', disabled: false, dataset: {},
    listeners: {}, focus() {},
    addEventListener(event, callback) { this.listeners[event] = callback; },
    setAttribute() {}, ...extra
  };
}

const token = element({ value: 'fake-token', type: 'password' });
const status = element();
const toggle = element();
const buttons = ['1', '2', '3', 'leave'].map(house => element({ dataset: { house } }));
const nodes = { '#token': token, '#status': status, '#toggle': toggle };
const calls = [];
const document = {
  querySelector: selector => nodes[selector],
  querySelectorAll: () => buttons
};
runInNewContext(script, {
  document, setTimeout, clearTimeout, AbortController,
  fetch: async (url, options) => {
    calls.push({ url, options });
    return { ok: false, status: 401 };
  }
});

await buttons[0].listeners.click();
assert.equal(calls.length, 1);
assert.equal(calls[0].options.method, 'POST');
assert.equal(calls[0].options.body, JSON.stringify({ house_id: 1 }));
assert.match(status.textContent, /401|認証/);
assert.ok(!status.textContent.includes('fake-token'), 'error should not reveal token');
assert.equal(token.value, '', 'token should be cleared after failure');
assert.equal(token.type, 'password', 'token should be hidden after failure');
assert.ok(buttons.every(button => !button.disabled), 'buttons should be restored');
