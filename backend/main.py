from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  
from controllers import login, libro_controller, usuario_controller, prestamo_controller, notificacion_controller, laptop_controller

app = FastAPI()

# ✅ Configurar CORS para permitir peticiones desde cualquier origen
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Incluir los controladores (Routers)
app.include_router(login.router)  
app.include_router(libro_controller.router)
app.include_router(usuario_controller.router)
app.include_router(prestamo_controller.router)
app.include_router(notificacion_controller.router)
app.include_router(laptop_controller.router)

# ✅ Ruta raíz para verificar que el backend funciona correctamente
@app.get("/")
def root():
    return {"message": "Sistema de Biblioteca funcionando correctamente :)))"}
