from fastapi import FastAPI
from pydantic import BaseModel, Field, EmailStr
from datetime import date, datetime
from typing import Optional

app = FastAPI()

# =========================================
# MODELO USUARIO
# =========================================
class Usuario(BaseModel):
    id: int = Field(gt=0)
    nombre: str = Field(min_length=3, max_length=50)
    correo: EmailStr
    contraseña: str = Field(min_length=8, description="Mínimo 8 caracteres")
    edad: int = Field(gt=10, lt=100)
    rol: str = Field(min_length=3, description="Jugador, admin o propietario")

# =========================================
# MODELO PROPIETARIO
# =========================================
class Propietario(BaseModel):
    id: int = Field(gt=0)
    nombre_negocio: str = Field(min_length=3, max_length=100)
    direccion: str = Field(min_length=5)
    telefono: str = Field(min_length=7, max_length=15)
    correo: EmailStr

# =========================================
# MODELO TORNEO
# =========================================
class Torneo(BaseModel):
    id: int = Field(gt=0)
    nombre_torneo: str = Field(min_length=5, max_length=100)
    tipo: str = Field(min_length=3)
    nivel: str = Field(min_length=3)
    fecha: date
    cupos: int = Field(gt=0)
    premio: float = Field(gt=0)

# =========================================
# MODELO INSCRIPCION
# =========================================
class Inscripcion(BaseModel):
    id: int = Field(gt=0)
    jugador: str = Field(min_length=3)
    torneo: str = Field(min_length=3)
    fecha_inscripcion: datetime
    pago_realizado: bool

# =========================================
# MODELO PAGO
# =========================================
class Pago(BaseModel):
    id: int = Field(gt=0)
    usuario: str = Field(min_length=3)
    monto: float = Field(gt=0)
    metodo_pago: str = Field(min_length=3)
    fecha_pago: datetime

# =========================================
# MODELO NOTIFICACION
# =========================================
class Notificacion(BaseModel):
    id: int = Field(gt=0)
    titulo: str = Field(min_length=3)
    mensaje: str = Field(min_length=5)
    fecha_envio: datetime

# =========================================
# MODELO RESULTADO
# =========================================
class Resultado(BaseModel):
    id: int = Field(gt=0)
    torneo: str = Field(min_length=3)
    ganador: str = Field(min_length=3)
    puntos: int = Field(ge=0)

# =========================================
# MODELO CANCHA
# =========================================
class Cancha(BaseModel):
    id: int = Field(gt=0)
    nombre_cancha: str = Field(min_length=3)
    ubicacion: str = Field(min_length=5)
    capacidad: int = Field(gt=0)
    disponible: bool

# =========================================
# MODELO REPORTE
# =========================================
class Reporte(BaseModel):
    id: int = Field(gt=0)
    tipo_reporte: str = Field(min_length=3)
    fecha_generacion: datetime
    descripcion: str = Field(min_length=5)

# =========================================
# RUTA PRINCIPAL
# =========================================
@app.get("/")
def inicio():
    return {
        "mensaje": "Bienvenido a MECHAPP API 🏆"
    }

# =========================================
# RUTAS USUARIOS
# =========================================
@app.post("/usuarios")
def crear_usuario(usuario: Usuario):
    return {
        "mensaje": "Usuario registrado correctamente",
        "usuario": usuario
    }

# =========================================
# RUTAS PROPIETARIOS
# =========================================
@app.post("/propietarios")
def crear_propietario(propietario: Propietario):
    return {
        "mensaje": "Propietario registrado correctamente",
        "propietario": propietario
    }

# =========================================
# RUTAS TORNEOS
# =========================================
@app.post("/torneos")
def crear_torneo(torneo: Torneo):
    return {
        "mensaje": "Torneo creado exitosamente",
        "torneo": torneo
    }

# =========================================
# RUTAS INSCRIPCIONES
# =========================================
@app.post("/inscripciones")
def crear_inscripcion(inscripcion: Inscripcion):
    return {
        "mensaje": "Inscripción realizada correctamente",
        "inscripcion": inscripcion
    }

# =========================================
# RUTAS PAGOS
# =========================================
@app.post("/pagos")
def crear_pago(pago: Pago):
    return {
        "mensaje": "Pago registrado correctamente",
        "pago": pago
    }

# =========================================
# RUTAS NOTIFICACIONES
# =========================================
@app.post("/notificaciones")
def crear_notificacion(notificacion: Notificacion):
    return {
        "mensaje": "Notificación enviada correctamente",
        "notificacion": notificacion
    }

# =========================================
# RUTAS RESULTADOS
# =========================================
@app.post("/resultados")
def crear_resultado(resultado: Resultado):
    return {
        "mensaje": "Resultado registrado correctamente",
        "resultado": resultado
    }

# =========================================
# RUTAS CANCHAS
# =========================================
@app.post("/canchas")
def crear_cancha(cancha: Cancha):
    return {
        "mensaje": "Cancha registrada correctamente",
        "cancha": cancha
    }

# =========================================
# RUTAS REPORTES
# =========================================
@app.post("/reportes")
def crear_reporte(reporte: Reporte):
    return {
        "mensaje": "Reporte generado correctamente",
        "reporte": reporte
    }

# =========================================
# RUTA ADICIONAL - LISTAR TORNEOS
# =========================================
@app.get("/torneos")
def listar_torneos():
    return {
        "torneos": [
            {
                "id": 1,
                "nombre_torneo": "Torneo Nacional de Tejo",
                "tipo": "Profesional",
                "nivel": "Avanzado",
                "cupos": 16
            }
        ]
    }

# =========================================
# RUTA ADICIONAL - LISTAR JUGADORES
# =========================================
@app.get("/usuarios")
def listar_usuarios():
    return {
        "usuarios": [
            {
                "id": 1,
                "nombre": "Carlos Pérez",
                "correo": "carlos@gmail.com",
                "rol": "Jugador"
            }
        ]
    }