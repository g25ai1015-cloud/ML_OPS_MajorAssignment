# End-to-End MLOps Pipeline for Face Recognition Classification

**CI Workflow | Dockerized Deployment | Kubernetes Orchestration**

This repository presents a complete Machine Learning Operations (MLOps) workflow developed as part of the MLOps Major Assignment. The project demonstrates the full machine learning lifecycle, including model training, automated Continuous Integration (CI), Docker-based containerization, and resilient deployment using Kubernetes.

 🚀 Project Links

**GitHub Repository:**
[Add GitHub Repository Link Here]

**Docker Hub Repository:**
[Add Docker Hub Repository Link Here]
📌 Key Features & System Architecture

 Model Development (`dev` branch)

* Implements a **Decision Tree Classifier** using the **Olivetti Faces Dataset** from scikit-learn.
* Follows a strict **70:30 train-test split** for model development and evaluation.
* Stores the trained model artifact using **joblib serialization** as `savedmodel.pth`.
* Includes dedicated scripts for both model training and performance validation.

 Continuous Integration (CI)

* Automated through **GitHub Actions** using the workflow definition located in `.github/workflows/ci.yml`.
* Executes automatically whenever new code is pushed to the repository.
* Creates an isolated execution environment, installs required dependencies, and runs training and testing workflows.
* Ensures code quality and verifies successful model execution before deployment.

 Containerization (`docker_cicd` branch)

* Packages the application inside a lightweight Docker image built on `python:3.9-slim`.
* Hosts a Flask-based web application for serving predictions.
* Provides a simple user interface that allows image uploads and returns predicted face classification labels.
* Ensures portability and consistency across different deployment environments.

 Kubernetes Deployment & Reliability

* Uses Kubernetes deployment manifests defined in `k8s-deployment.yaml`.
* Maintains a minimum of **three running replicas** to improve availability and load distribution.
* Supports automatic pod recovery through Kubernetes self-healing mechanisms.
* Ensures uninterrupted service by replacing failed or terminated pods without manual intervention.



 📁 Repository Structure & Branch Organization

The repository follows a structured multi-branch workflow to separate development, deployment, and production-related components.

 `main`

Contains the base repository configuration and project documentation.

 `dev`

Includes machine learning development resources:

* `train.py`
* `test.py`
* GitHub Actions CI workflow configuration

 `docker_cicd`

Contains deployment and delivery components:

* Flask application (`app.py`)
* Docker configuration (`Dockerfile`)
* Kubernetes deployment resources (`k8s-deployment.yaml`)



```text
.
├── .github/
│   └── workflows/
│       └── ci.yml              # GitHub Actions CI pipeline
├── app.py                      # Flask application entry point
├── train.py                    # Model training script
├── test.py                     # Model evaluation and testing script
├── requirements.txt            # Project dependencies
├── Dockerfile                  # Docker image build configuration
├── k8s-deployment.yaml         # Kubernetes deployment and service manifest
├── .gitignore                  # Ignored files and directories
└── README.md                   # Project documentation


 ⚙️ Technology Stack

* Python
* Scikit-learn
* Flask
* GitHub Actions
* Docker
* Kubernetes
* Joblib

 🎯 Project Objectives

* Develop and evaluate a machine learning model using the Olivetti Faces dataset.
* Automate training and testing workflows through Continuous Integration.
* Containerize the application for consistent deployment.
* Deploy the solution using Kubernetes with high availability and fault tolerance.
* Demonstrate a complete end-to-end MLOps workflow from development to production deployment.
