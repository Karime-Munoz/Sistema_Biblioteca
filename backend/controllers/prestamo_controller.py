from fastapi import APIRouter, HTTPException
from dao.supabase_client import supabase
from model.prestamo import Prestamo
from datetime import datetime, timedelta

router = APIRouter()

@router.post("/prestamos")
def solicitar_prestamo(prestamo: Prestamo):
    try:
        print("📌 Datos recibidos en el backend:", prestamo.dict())

        item = None
        tipo = None

        libro = supabase.table("libros").select("estado, titulo, autor").eq("id", prestamo.item_id).execute()
        if libro.data and libro.data[0]["estado"] == "disponible":
            item = libro.data[0]
            tipo = "libro"
        
        laptop = supabase.table("laptops").select("estado, marca, modelo").eq("id", prestamo.item_id).execute()
        if laptop.data and laptop.data[0]["estado"] == "disponible":
            item = laptop.data[0]
            tipo = "laptop"

        if not item:
            raise HTTPException(status_code=400, detail="El item no está disponible para préstamo.")

        fecha_inicio = datetime.now().strftime("%Y-%m-%d")
        fecha_fin = (datetime.now() + timedelta(days=14)).strftime("%Y-%m-%d")

        supabase.table("prestamos").insert({
            "matricula": prestamo.matricula,
            "item_id": prestamo.item_id,
            "titulo": item.get("titulo", item.get("marca", "Equipo")),
            "autor": item.get("autor", item.get("modelo", "Modelo desconocido")),
            "fecha_inicio": fecha_inicio,
            "fecha_fin": fecha_fin,
            "tipo": tipo
        }).execute()

        tabla = "libros" if tipo == "libro" else "laptops"
        supabase.table(tabla).update({"estado": "prestado"}).eq("id", prestamo.item_id).execute()

        return {"message": f"✅ {tipo.capitalize()} prestado con éxito"}

    except Exception as e:
        print("❌ Error en el backend:", str(e))
        raise HTTPException(status_code=500, detail=str(e))
