from fastapi import FastAPI, Response, Cookie
from fastapi.responses import JSONResponse
import uvicorn  # Added for running the app
import os
from typing import Optional  # Added for type hinting

app = FastAPI()


@app.get("/")
def index():
    return "Hello from the backend!"


@app.get("/health")
def health():
    return Response(content="OK", media_type="text/plain", status_code=200)


@app.get("/sticky")
def sticky(awsalb: str | None = Cookie(None)):
    # In FastAPI, cookies are accessed via parameters with Cookie()
    return JSONResponse({"sticky_session": bool(awsalb), "session_id": awsalb})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 80))
    uvicorn.run(app, host="0.0.0.0", port=port)
