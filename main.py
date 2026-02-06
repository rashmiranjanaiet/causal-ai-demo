from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI(title="Causal AI Demo")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )

@app.post("/analyze", response_class=HTMLResponse)
def analyze(
    request: Request,
    conversation: str = Form(...)
):
    # Demo logic (replace later with AI)
    result = "Delay occurred because verification was requested."

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "result": result,
            "conversation": conversation
        }
    )

