# Two-Tier Flask + MySQL Application with Jenkins CI/CD

Prajwal Muthaye
This project demonstrates a **Two-Tier Web Application** using **Flask (Python)** as the frontend/backend service and **MySQL** as the database, deployed and automated using **Jenkins CI/CD** on an **AWS EC2 instance**.

---

## 📌 Project Overview

* **Tier 1 (Application Layer):** Flask web application (Python)
* **Tier 2 (Database Layer):** MySQL database
* **CI/CD Tool:** Jenkins
* **Version Control:** Git & GitHub
* **Server:** AWS EC2 (Ubuntu)

---

## 🛠 Technologies Used

* Python 3
* Flask
* MySQL
* mysql-connector-python
* Jenkins
* Git & GitHub
* Docker 
* AWS EC2

---

## 📂 Project Structure

```
two-tier-app/
│
├── app.py              
├── requirements.txt      
├── Jenkinsfile            
├── Dockerfile            
├── docker-compose.yml     
└── README.md              
```

---

## ⚙️ Step-by-Step Setup Guide

### 🔹 Step 1: Launch EC2 Instance

* Launch Ubuntu 
* Open inbound ports:

  * `22` (SSH)
  * `8080` (Jenkins)
  * `5000` (Flask app)
---
### 🔹 Step 2: Install System Dependencies

```bash
sudo apt update
sudo apt install -y python3 python3-pip git
sudo apt install -y python3 python3-pip git docker.io docker-compose mysql-client
sudo systemctl start docker
sudo systemctl enable docker
```
---
### 🔹 Step 3: Install Flask & MySQL Connector

```bash
pip3 install flask mysql-connector-python
```

### 🔹 Step 4: Create Flask Application (app.py)

```python
from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route('/')
def home():
    return "Two-Tier Flask App is Running"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

---

### 🔹 Step 5: Create requirements.txt

```
flask
mysql-connector-python
```

---

### 🔹 Step 6: Run Application Locally

```bash
python3 app.py
```

Access in browser:

```
http://<EC2-PUBLIC-IP>:5000
```

---

## 🚀 Jenkins CI/CD Setup

### 🔹 Step 7: Install Jenkins

```bash
sudo apt install -y openjdk-17-jdk
wget -q -O - https://pkg.jenkins.io/debian-stable/jenkins.io.key | sudo apt-key add -
sudo sh -c 'echo deb https://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list'
sudo apt update
sudo apt install -y jenkins
sudo systemctl start jenkins
```

Access Jenkins:

```
http://<EC2-PUBLIC-IP>:8080
```

---

### 🔹 Step 8: Unlock Jenkins

```bash
sudo cat /var/lib/jenkins/secrets/initialAdminPassword
```

Install suggested plugins and create admin user.

---

### 🔹 Step 9: Jenkinsfile (Pipeline)

```groovy
pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }
        stage('Run Application') {
            steps {
                sh 'python3 app.py &'
            }
        }
    }
}
```

---

### 🔹 Step 10: Create Jenkins Pipeline Job

1. Jenkins Dashboard → New Item
2. Name: `two-tier-cicd`
3. Select **Pipeline**
4. Choose **Pipeline script from SCM**
5. Provide GitHub repo URL
6. Branch: `main`
7. Script Path: `Jenkinsfile`

---

### 🔹 Step 11: Build Pipeline

Click **Build Now**

* ✅ Blue → SUCCESS
* ❌ Red → Check Console Output

---


## 📈 Final Outcome

* Flask app accessible via browser
* Jenkins automates build & deployment
* Two-tier architecture successfully implemented

---

