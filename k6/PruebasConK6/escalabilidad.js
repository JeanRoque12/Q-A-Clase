import http from 'k6/http';
import { sleep } from 'k6';

export let options = {
    stages: [
        { duration: '1m', target: 10 },  // Inicio con 10 usuarios
        { duration: '2m', target: 100 }, // Incremento a 100 usuarios
        { duration: '2m', target: 200 }, // Máximo de 200 usuarios
        { duration: '1m', target: 0 },   // Reducción gradual
    ],
};

export default function () {
    http.get('https://httpbin.org/');
    sleep(1);
}

