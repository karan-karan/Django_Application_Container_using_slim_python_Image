# Django Application Containerized Using Slim Python Image

This project demonstrates how to deploy a Django application inside a Docker container using the lightweight `python:3.10-slim` image. The guide includes steps for setting up an EC2 instance, installing Docker, building the image, running the container, and pushing it to Docker Hub.

---

## 🖥️ Step 1: Create EC2 Instance (Ubuntu)

Launch an Ubuntu EC2 instance (t2.micro / free tier).

Update packages:

```bash
sudo apt update
```
---

## 🐳 Step 2: Install Docker
```bash
sudo apt install docker.io -y
```

Check Docker is installed and running:
```bash
systemctl status docker
```

## 👤 Step 3: Add Ubuntu User to Docker Group
Docker runs as root by default. To run Docker without sudo:
```bash
sudo usermod -aG docker ubuntu
```

Restart Docker to apply changes:
```bash
sudo systemctl restart docker
```

Logout and login again (or reboot EC2):
```bash
sudo reboot
```

## 📥 Step 4: Clone the GitHub Repository
```bash
git clone https://github.com/karan-karan/Django_Application_Container_using_slim_python_Image.git
cd Django_Application_Container_using_slim_python_Image
```

## 🏗️ Step 5: Build Docker Image
```bash
docker build -t djangoapp:latest .
```

## ▶️ Step 6: Run the Container
Expose Django container port 8000 to EC2 port 80:
```bash
docker run -d -p 80:8000 --name mydjangoapp djangoapp:latest
```

## 🌐 Step 7: Access the Application
Open in browser:
```bash
http://<EC2_PUBLIC_IP>/
```

## 🐳 Step 8: Push Image to Docker Hub
Login to Docker Hub
Generate a Docker Personal Access Token:

➡️ https://hub.docker.com/settings/security

Go to Personal access tokens → Generate token
Login using the token


Tag the Image
```bash
docker tag djangoapp:latest karantanwar/djangoapp:latest
```

Push to Docker Hub
```bash
docker push karantanwar/djangoapp:latest
```



🎉 Done!
Django app is now:

✅ Containerized
⚡ Running on EC2
☁️ Published on Docker Hub



# ⚠️ Issue Faced: Invalid HTTP_HOST Header
Django threw an error:
Invalid HTTP_HOST header: '13.127.255.7:80'
This happens because the IP is not added in ALLOWED_HOSTS in settings.py.

Fix:
To allow all hosts:
ALLOWED_HOSTS = ['*']
OR
To allow only your EC2 IP:
ALLOWED_HOSTS = ['13.127.255.7']



## 📌 Commands Summary
sudo apt update
sudo apt install docker.io -y
systemctl status docker
sudo usermod -aG docker ubuntu
sudo systemctl restart docker
git clone <repo-url>
docker build -t djangoapp:latest .
docker run -d -p 80:8000 --name mydjangoapp djangoapp:latest
docker login
docker tag djangoapp:latest karantanwar/djangoapp:latest
docker push karantanwar/djangoapp:latest


# 📘 Author

Karan, DevOps Engineer 🚀
