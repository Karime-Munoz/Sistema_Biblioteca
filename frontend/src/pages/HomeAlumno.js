import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom"; 
import axios from "axios";
import "../styles/HomeAlumno.css";

function HomeAlumno() {
  const [libros, setLibros] = useState([]);
  const [search, setSearch] = useState("");
  const [misPrestamos, setMisPrestamos] = useState([]);
  const navigate = useNavigate(); 


  useEffect(() => {
    axios.get("http://127.0.0.1:8000/libros")
      .then(response => setLibros(response.data))
      .catch(error => console.error("❌ Error cargando libros:", error));
  }, []);

  
  useEffect(() => {
    axios.get("http://127.0.0.1:8000/prestamos?matricula=A12345") 
      .then(response => setMisPrestamos(response.data))
      .catch(error => console.error("❌ Error cargando préstamos:", error));
  }, []);


  const solicitarPrestamo = (libroId) => {
    axios.post("http://127.0.0.1:8000/prestamos", { item_id: libroId, matricula: "A12345" }) 
      .then(() => {
        alert("✅ Préstamo solicitado con éxito");
        setLibros(libros.map(libro => 
          libro.id === libroId ? { ...libro, estado: "prestado" } : libro
        ));
      })
      .catch(error => alert("❌ Error al solicitar préstamo: " + error.message));
  };


  const cerrarSesion = () => {
    navigate("/");
  };

  return (
    <div className="home-alumno-container">
      <button className="logout-button" onClick={cerrarSesion}>Cerrar Sesión</button>


      <div className="search-bar">
        <input
          type="text"
          placeholder="Buscar por título o autor..."
          value={search}
          onChange={(e) => setSearch(e.target.value)}
        />
      </div>

      <div className="spacer"></div>

      
      <div className="libros-list">
        <h2>📚 Libros Disponibles</h2>
        {libros.length > 0 ? (
          <ul>
            {libros
              .filter((libro) =>
                libro.titulo.toLowerCase().includes(search.toLowerCase()) ||
                libro.autor.toLowerCase().includes(search.toLowerCase())
              )
              .map((libro) => (
                <li key={libro.id} className="libro-item">
                  <div className="libro-info">
                    <strong>{libro.titulo}</strong> - {libro.autor}
                  </div>
                  {libro.estado === "disponible" ? (
                    <button className="btn-prestamo" onClick={() => solicitarPrestamo(libro.id)}>
                      Solicitar Préstamo
                    </button>
                  ) : (
                    <span className="prestado-label">No disponible</span>
                  )}
                </li>
              ))}
          </ul>
        ) : (
          <p>No hay libros disponibles</p>
        )}
      </div>

      
      <div className="prestamos-list">
        <h2>📖 Mis Préstamos</h2>
        {misPrestamos.length > 0 ? (
          <ul>
            {misPrestamos.map((prestamo) => (
              <li key={prestamo.id} className="prestamo-item">
                <div>
                  <strong>{prestamo.titulo}</strong> - {prestamo.autor}
                  <p>📅 Inicio: {prestamo.fecha_inicio} | 📅 Fin: {prestamo.fecha_fin}</p>
                </div>
              </li>
            ))}
          </ul>
        ) : (
          <p>No tienes préstamos activos</p>
        )}
      </div>
    </div>
  );
}

export default HomeAlumno;