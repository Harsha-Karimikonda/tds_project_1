import os
from pathlib import Path
from dotenv import load_dotenv

try:
    load_dotenv()
except Exception as e:
    print(f"Error loading .env file: {e}")

# API Configuration
API_HOST = "0.0.0.0"  # Changed to allow external access
API_PORT = 8000  # Standard HTTPS port

# LLM Configuration
AIPROXY_TOKEN = os.getenv("AIPROXY_TOKEN")
if not AIPROXY_TOKEN:
    raise ValueError("AIPROXY_TOKEN environment variable is not set")

# File System
DATA_DIR = Path("./data")