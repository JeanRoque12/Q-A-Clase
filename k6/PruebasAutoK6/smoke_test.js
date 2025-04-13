// smoke_test.js
import http from 'k6/http';
import { check } from 'k6';

export let options = {
  vus: 10,               
  duration: '30s',       
};

export default function () {
  let res = http.get('https://httpbin.org/get');
  check(res, {
    'status es 200': (r) => r.status === 200,
  });
}

