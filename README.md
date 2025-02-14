# Install Ollama on Ubuntu

Follow these steps to install Ollama and set up the project on an Ubuntu server.

## Step 1: Update Ubuntu Server

Run the following command to update your Ubuntu server:
```bash
sudo apt update
```

## Step 2: Install Ollama Service

### Install Ollama
Run this command to install Ollama:
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

### Download the Model
Run the following command to download the required model:
```bash
ollama run llama3.2
```

## Step 3: Download the Project Repository

Clone the project repository:
```bash
git clone git@192.168.0.69:machine-learning/development/ollama_api.git
cd ollama_api
```

## Step 4: Set Up the Environment

### Create Virtual Environment
Run the following command to create a virtual environment:
```bash
python3.12 -m venv venv
```

### Activate the Virtual Environment
Activate the virtual environment:
```bash
source venv/bin/activate
```

### Install Dependencies
Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Step 5: Run the Project

Run the project using the following command:
```bash
python main.py
```

Your Ollama project is now set up and running!

