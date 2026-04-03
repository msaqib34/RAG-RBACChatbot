from typing import Dict

from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials




app = FastAPI()
security = HTTPBasic()

# Dummy user database
users_db: Dict[str, Dict[str, str]] = {
    "Tony": {"password": "password123", "role": "engineering"},
    "Bruce": {"password": "securepass", "role": "marketing"},
    "Sam": {"password": "financepass", "role": "finance"},
    "Peter": {"password": "pete123", "role": "engineering"},
    "Sid": {"password": "sidpass123", "role": "marketing"},
    "Natasha": {"password": "hrpass123", "role": "hr"}
}



# Authentication dependency
def authenticate(credentials: HTTPBasicCredentials = Depends(security)):
    username = credentials.username
    password = credentials.password
    user = users_db.get(username)
    if not user or user["password"] != password:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"username": username, "role": user["role"]}



####################### Login and Protected Endpoints #######################

# Login endpoint
@app.get("/login")
def login(user=Depends(authenticate)):
    return {"message": f"Welcome {user['username']}!", "role": user["role"]}


# Protected test endpoint
@app.get("/test")
def test(user=Depends(authenticate)):
    return {"message": f"Hello {user['username']}! You can now chat.", "role": user["role"]}


# # Protected chat endpoint
# @app.post("/chat")
# def query(user=Depends(authenticate), message: str = "Hello"):
#     return "Implement this endpoint."

# Get Current User Endpoint (for testing purposes)
def get_current_user(credentials: HTTPBasicCredentials = Depends(security)):
    return {"username": credentials.username, "role": "user"}  # temp



@app.post("/chat")
def chat(message: str, user=Depends(get_current_user)):
    role = user["role"]
    print("USER:", user)

    # 🔥 Call your function here
    docs = retrieve_docs(message, role)

    # Combine docs into response (temporary RAG)
    return {
        "response": f"Answer based on: {docs}",
        "sources": docs,
        "role": role
    }
    # if role == "engineering":
    #     # Simulate engineering-specific response
    #     return {
    #         "response": f"Engineering response to: {message}",
    #         "role": role
    #     }
    # elif role == "marketing":
    #     # Simulate marketing-specific response
    #     return {
    #         "response": f"Marketing response to: {message}",
    #         "role": role
    #     }   
    # elif role == "finance":
    #     # Simulate finance-specific response
    #     return {
    #         "response": f"Finance response to: {message}",
    #         "role": role
    #     }   
    # elif role == "hr":
    #     # Simulate HR-specific response
    #     return {
    #         "response": f"HR response to: {message}",
    #         "role": role
    #     }
    # else:
    #     raise HTTPException(status_code=403, detail="Unauthorized role")
    

def retrieve_docs(message, role):
    
    print("Inside retrieve_docs")
    print("ROLE:", role)
    print("MESSAGE:", message)

    role = role.lower()

    message = message.lower()

    if role == "engineering":
        if "api" in message or "system" in message:
            return ["System Design Doc", "API Architecture"]
        elif "bug" in message:
            return ["Debugging Guide"]
        else:
            return ["General Engineering Doc"]

    elif role == "marketing":
        if "campaign" in message:
            return ["Campaign Strategy", "Ad Performance"]
        elif "seo" in message:
            return ["SEO Guide"]
        else:
            return ["Marketing Overview"]

    elif role == "finance":
        if "budget" in message:
            return ["Budget Report"]
        elif "revenue" in message:
            return ["Revenue Sheet"]
        else:
            return ["Finance Summary"]

    elif role == "hr":
        if "leave" in message:
            return ["Leave Policy"]
        elif "hiring" in message:
            return ["Hiring Process"]
        else:
            return ["HR Handbook"]
    

