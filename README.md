# 🚀 LLM-based Automation Agent  

Welcome to the **LLM-based Automation Agent**! This intelligent automation agent leverages natural language processing and LLM capabilities to handle a variety of tasks seamlessly.  

---

## 🌟 Features  
- 🤖 **Task Parsing**: Powered by GPT-4o-Mini for accurate task interpretation.  
- 🔒 **Secure File Operations**: Ensures safe and secure handling of sensitive files.  
- ⚡ **Multi-Task Support**: Efficiently handles multiple task types.  
- 🌐 **API-Based Execution**: Executes tasks using powerful API integrations.  

---

## 📋 Prerequisites  
Make sure you have the following installed:  
- **Docker**: For containerization and deployment.  
- **AI Proxy Token**: Required for accessing LLM functionalities.  

---

## ⚙️ Installation & Run  

### 1. Clone the Repository  
```sh
git clone https://github.com/anony0900/my-llm.git
```
``` 
cd my-llm 
```

### 2. Install Dependencies  
```
pip install -r requirements.txt  
```

### 3. Setup Environment Variables  
### Create a .env file in the project root  
```
echo "AIPROXY_TOKEN=your_token_here" > .env  
```

### 4. Run Locally  
```
python run.py  
```

### 5. Using Docker  
### Build the image  
```
docker build -t llm-agent .  
```

### Run the container  
```
docker run --env-file .env -p 8000:8000 llm-agent  
```
