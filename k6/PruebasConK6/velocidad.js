import http from 'k6/http';
import { check } from 'k6';

export let options = {
    vus: 10,
    duration: '30s',
};

export default function () {
    let res = http.get('https://httpbin.org/');
    check(res, {
        'status es 200': (r) => r.status === 200,
        'respuesta en menos de 300ms': (r) => r.timings.duration < 300,
    });
}

