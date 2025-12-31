# 📞 Contacts Management System on Kubernetes

## Project Description
This project is a **RESTful API** built with **FastAPI** (Python) and **MongoDB** for managing a contacts book. It allows users to perform full CRUD operations (Create, Read, Update, Delete) on contact records.

The application is containerized using **Docker** and orchestrated using **Kubernetes**.

### API Endpoints
| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/contacts` | Retrieve all contacts |
| `POST` | `/contacts` | Create a new contact |
| `PUT` | `/contacts/{id}` | Update an existing contact |
| `DELETE` | `/contacts/{id}` | Delete a contact |

---

## ✅ Prerequisites
Before you begin, ensure you have the following installed:
* **Docker** - To build the application image.
* **Minikube** (or Docker Desktop with Kubernetes enabled) - To run the cluster locally.
* **kubectl** - Command-line tool for interacting with the Kubernetes cluster.

---

## ⚙️ Setup Instructions

### 1. Build the Docker Image
First, build the image using the tag specified in your Kubernetes deployment (`api-pod.yaml`).

```bash
docker build -t kobigdocker/mongo-api:latest .
Note: If you are using Minikube, you might need to load the image into Minikube's environment:

Bash

minikube image load kobigdocker/mongo-api:latest
2. Deploy to Kubernetes
Apply the configuration files to your cluster. It is recommended to deploy the Database first, then the API.

Bash

# 1. Deploy MongoDB Pod and Service
kubectl apply -f k8s/mongodb-pod.yaml
kubectl apply -f k8s/mongodb-service.yaml

# 2. Deploy API Pod and Service
kubectl apply -f k8s/api-pod.yaml
kubectl apply -f k8s/api-service.yaml
3. Verify Deployment
Check that all pods are running:

Bash

kubectl get pods
Wait until status is Running.

🧪 Testing Instructions (curl commands)
The API is exposed via NodePort 30081. You can run the following commands in your terminal to test the endpoints.

1. Create a New Contact (POST)
Bash

curl -X POST "http://localhost:30081/contacts" \
     -H "Content-Type: application/json" \
     -d "{\"first_name\": \"Israel\", \"last_name\": \"Israeli\", \"phone_number\": \"050-1234567\"}"
2. Get All Contacts (GET)
Bash

curl -X GET "http://localhost:30081/contacts"
Copy the id from the response for the next steps.

3. Update a Contact (PUT)
Replace <YOUR_ID> with the ID you received from the previous step.

Bash

curl -X PUT "http://localhost:30081/contacts/<YOUR_ID>" \
     -H "Content-Type: application/json" \
     -d "{\"first_name\": \"Moshe\", \"last_name\": \"Cohen\", \"phone_number\": \"054-9876543\"}"
4. Delete a Contact (DELETE)
Replace <YOUR_ID> with the ID you want to delete.

Bash

curl -X DELETE "http://localhost:30081/contacts/<YOUR_ID>"
🧹 Cleanup
To remove all resources:

Bash

kubectl delete -f k8s/