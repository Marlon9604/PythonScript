###pip install locustio
###locust -f clases/locustfile.py  --host=https://jsonplaceholder.typicode.com
import consumocsv as arch
from locust import HttpLocust, TaskSet, task

class UserBehavior(TaskSet):
    
    archivo = arch.LecturaCSV()

    # def on_start(self):
    #     """ on_start is called when a Locust start before any task is scheduled """
    #     self.login()

    # def on_stop(self):
    #     """ on_stop is called when the TaskSet is stopping """
    #     self.logout()

    # def login(self):
    #     self.client.post("/posts2", {"username":"ellen_key", "password":"education"})

    # def logout(self):
    #     self.client.post("/logout", {"username":"ellen_key", "password":"education"})

    @task(2)
    def index(self):
        valores = self.archivo.leer(0,3)[0]
        self.client.get(f"/api/EntidadPrestadora/Consultar/idLocalizacion/{valores}")

    @task(1)
    def profile(self):
        self.client.get("/api/Entidades/ConsultarEntidadesLista/localizacion/1")

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000 ##milisegundos tiempo de espera entre cada peticio del un usario
    max_wait = 9000
