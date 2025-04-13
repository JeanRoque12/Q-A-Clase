from locust import HttpUser, task, between

class LoadTest(HttpUser):
    wait_time = between(1, 3)  # Tiempo de espera entre solicitudes (1 a 3 segundos)

    @task
    def get_status(self):
        self.client.get("/status/200")  # Realiza una solicitud GET a la URL https://httpbin.org/status/200

