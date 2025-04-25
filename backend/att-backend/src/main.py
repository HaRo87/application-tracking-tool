from fastapi import FastAPI

app = FastAPI(
    title="Application Tracking Tool",
    version=0.1,
    description="A tool which helps in tracking job applications.",
)

@app.get("/")
def get_root():
    """Root entry point"""
    return {"Application Tracking Tool": "Welcome!"}
