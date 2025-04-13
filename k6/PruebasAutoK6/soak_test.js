// soak_test.js
import http from 'k6/http';
import { check, sleep } from 'k6';

export let options = {
  vus: 100,              
  duration: '30m',       
};

export default function () {
  let res = http.get('https://httpbin.org/get');
  check(res, {
    'status es 200': (r) => r.status === 200,
  });
  sleep(1);
}

