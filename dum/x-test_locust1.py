
# # from selenium import webdriver
# from selenium.webdriver.common.by import By

# # driver = webdriver.Chrome()  # ChromeDriver ต้องอยู่ใน PATH
# # driver.get("https://www.google.com")
# # driver.quit()

# from locust import HttpUser, task, between

# # สร้าง class User (จำลองผู้ใช้งาน 1 คน)
# class WebsiteUser(HttpUser):
#     # ระหว่าง task แต่ละรอบ รอแบบสุ่ม 1-5 วินาที
#     wait_time = between(1, 5)

#     @task
#     def load_homepage(self):
#         # ผู้ใช้เปิดหน้า homepage
#         self.client.get("/")

#     @task
#     def load_products(self):
#         # ผู้ใช้เข้าไปดู products
#         self.client.get("/products")

#     @task
#     def login(self):
#         # ผู้ใช้พยายาม login
#         self.client.post("/login", {
#             "username": "test_user",
#             "password": "1234"
#         })


# #locust -f locustfile.py --host=http://example.com --headless -u 100 -r 10 -t 1m --csv=report
# #locust -f locustfile.py --host=http://example.com

# #python -m locust -f C:\Users\Cream\locust\locusttest.py --host=http://example.com