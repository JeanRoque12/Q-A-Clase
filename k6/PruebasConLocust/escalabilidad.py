from locust import HttpUser, task, between

class ScalabilityTest(HttpUser):
    wait_time = between(1, 3)  # Tiempo de espera entre solicitudes (1 a 3 segundos)

    @task
    def get_scalability(self):
        self.client.get("/delay/1")  # Realiza una solicitud GET a la URL https://httpbin.org/delay/1


