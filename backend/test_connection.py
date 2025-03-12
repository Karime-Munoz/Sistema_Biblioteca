import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "dao")))

from supabase_client import supabase  # Importar Supabase desde dao/

def test_connection():
    try:
        response = supabase.table("usuarios").select("*").limit(5).execute()
        
        if response.data:
            print("✅ Conexión a Supabase exitosa. Datos de prueba:")
            for usuario in response.data:
                print(f"ID: {usuario['id']}, Nombre: {usuario['nombre']}, Rol: {usuario['rol']}")
        else:
            print("⚠️ Conexión establecida, pero la tabla 'usuarios' está vacía.")

    except Exception as e:
        print(f"❌ Error en la conexión a Supabase: {e}")

if __name__ == "__main__":
    test_connection()
