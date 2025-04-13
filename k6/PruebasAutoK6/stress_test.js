// stress_test.js
import http from 'k6/http';
import { check, sleep } from 'k6';

export let options = {
  stages: [
    { duration: '1m', target: 50 }, 
    { duration: '2m', target: 100 }, 
    { duration: '2m', target: 150 }, 
    { duration: '2m', target: 0 },    
  ],
};

export default function () {
  let res = http.get('https://httpbin.org/get');
  check(res, {
    'status es 200': (r) => r.status === 200,
    'respuesta < 500ms': (r) => r.timings.duration < 500,
  });
  sleep(1);
}

