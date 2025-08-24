from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def load_home(self):
        self.client.get("/")

    @task
    def login(self):
        self.client.post("/login", {
            "username": "test_user",
            "password": "1234"
        })
