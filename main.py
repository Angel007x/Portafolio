from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Montar archivos estáticos (CSS, imágenes)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Configurar plantillas HTML
templates = Jinja2Templates(directory="templates")

# Datos de ejemplo para tus proyectos (puedes pasarlos dinámicamente)
PROYECTOS = [
    {
        "titulo": "Plataforma de Predicciones P2P",
        "descripcion": "Sistema de micro-predicciones en tiempo real con libro de órdenes, gestión de balances y lógica de desequilibrio.",
        "tecnologias": ["Python", "FastAPI", "React", "PostgreSQL"],
        "link": "https://github.com/tu-usuario/tu-proyecto"
    },
    {
        "titulo": "Sistema de Gestión Inmobiliaria",
        "descripcion": "Aplicación full-stack para administración de edificios, control de áreas comunes y reservas en tiempo real.",
        "tecnologias": ["Node.js", "React", "Tailwind CSS"],
        "link": "https://github.com/tu-usuario/tu-proyecto"
    }
]

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "proyectos": PROYECTOS})