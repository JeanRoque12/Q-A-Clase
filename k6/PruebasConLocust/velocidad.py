from locust import HttpUser, task, between

class ResponseTimeTest(HttpUser):
    wait_time = between(1, 2)  # Tiempo de espera entre solicitudes (1 a 2 segundos)

    @task
    def get_response(self):
        self.client.get("/get")  # Realiza una solicitud GET a la URL https://httpbin.org/get


