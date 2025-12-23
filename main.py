from fastapi import FastAPI, HTTPException
from module import Service

app = FastAPI()

services_data = [
    Service(id=1, name="IP Telephone", desc="hbdaknasdsad"),
    Service(id=2, name="Cloud", desc="asjassld;aa"),
    Service(id=3, name="Email Services", desc="lsadldas'owq"),
    Service(id=4, name="Web Hosting", desc="lwqwqddsmsdsmk")
]

@app.get("/")
def root():
    return {"message": "Hello FastAPI"}

@app.get("/services")
def get_services():
    return services_data

@app.get("/service/{id}")
def get_service(id: int):
    for service in services_data:
        if service.id == id:
            return service
    raise HTTPException(status_code=404, detail="Service not found")

@app.post("/service")
def add_service(service: Service):
    for s in services_data:
        if s.id == service.id:
            return "Service add successfully"
    services_data.append(service)
    return service


@app.put("/service/{id}")
def update_service(id: int,service: Service):
    for i in range(len(services_data)):
        if services_data[i].id==id:
            services_data[i]=service
            return "Update is successfull"
    return "There is no service"

@app.delete("/service/{id}")
def delete_service(id: int):
    for i in range(len(services_data)):
        if services_data[i].id==id:
            del services_data[i]
            return "Service deleted"
    return "There is no service"
    