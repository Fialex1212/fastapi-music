from fastapi.middleware.cors import CORSMiddleware

origin = ["http://localhost:3000", "http://localhost:8000"]

def add_cors(app):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origin,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )