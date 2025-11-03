import json
import os
from .configdns import REGISTRY_FILE

def load_registry():
    if not os.path.exists(REGISTRY_FILE):
        with open(REGISTRY_FILE, "w") as f:
            json.dump({}, f)
    try:
        with open(REGISTRY_FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("Registry file corrupted. Reinitializing.")
        with open(REGISTRY_FILE, "w") as f:
            json.dump({}, f)
        return {}

def save_registry(data):
    with open(REGISTRY_FILE, "w") as f:
        json.dump(data, f)
