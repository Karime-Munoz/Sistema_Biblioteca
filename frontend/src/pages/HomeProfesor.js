import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";
import "../styles/HomeProfesor.css";

function HomeProfesor() {
  const [libros, setLibros] = useState([]);
  const [laptops, setLaptops] = useState([]);
  const [misPrestamos, setMisPrestamos] = useState([]);
  const [search, setSearch] = useState(""); 
  const navigate = useNavigate();

  useEffect(() => {
    axios.get("http://127.0.0.1:8000/libros")
      .then(response => setLibros(response.data))
      .catch(error => console.error("❌ Error cargando libros:", error));

    axios.get("http://127.0.0.1:8000/laptops")
      .then(response => setLaptops(response.data))
      .catch(error => console.error("❌ Error cargando laptops:", error));

    axios.get("http://127.0.0.1:8000/prestamos?matricula=P56789")
      .then(response => setMisPrestamos(response.data))
      .catch(error => console.error("❌ Error cargando préstamos:", error));

  }, []);

  const solicitarPrestamo = (itemId, tipo) => {
    axios.post("http://127.0.0.1:8000/prestamos", { item_id: itemId, matricula: "P56789" })
      .then(() => {
        alert(`✅ ${tipo} prestado con éxito`);
        if (tipo === "Libro") {
          setLibros(libros.filter(libro => libro.id !== itemId));
        } else {
          setLaptops(laptops.filter(laptop => laptop.id !== itemId));
        }

        axios.get("http://127.0.0.1:8000/prestamos?matricula=P56789")
          .then(response => setMisPrestamos(response.data))
          .catch(error => console.error("❌ Error actualizando préstamos:", error));
      })
      .catch(error => alert(`❌ Error al solicitar ${tipo.toLowerCase()}: ${error.message}`));
  };

  const librosFiltrados = libros.filter(libro =>
    libro.titulo.toLowerCase().includes(search.toLowerCase()) ||
    libro.autor.toLowerCase().includes(search.toLowerCase())
  );

  const laptopsFiltradas = laptops.filter(laptop =>
    laptop.marca.toLowerCase().includes(search.toLowerCase()) ||
    laptop.modelo.toLowerCase().includes(search.toLowerCase())
  );

  return (
    <div className="home-profesor-container">
      <button className="logout-button" onClick={() => navigate("/")}>Cerrar Sesión</button>

      <div className="search-bar">
        <input
          type="text"
          placeholder="Buscar por título, autor o laptop..."
          value={search}
          onChange={(e) => setSearch(e.target.value)}
        />
      </div>

      <div className="items-list">
        <h2>📚 Libros Disponibles</h2>
        <ul>
          {librosFiltrados.map(libro => (
            <li key={libro.id} className="item">
              <div className="item-info">
                <strong>{libro.titulo}</strong> - {libro.autor}
              </div>
              <button className="btn-prestamo" onClick={() => solicitarPrestamo(libro.id, "Libro")}>
                Solicitar Préstamo
              </button>
            </li>
          ))}
        </ul>
        {librosFiltrados.length === 0 && <p>No hay libros disponibles.</p>}
      </div>

      <div className="items-list">
        <h2>💻 Laptops Disponibles</h2>
        <ul>
          {laptopsFiltradas.map(laptop => (
            <li key={laptop.id} className="item">
              <div className="item-info">
                <strong>{laptop.marca}</strong> - {laptop.modelo}
              </div>
              <button className="btn-prestamo" onClick={() => solicitarPrestamo(laptop.id, "Laptop")}>
                Solicitar Laptop
              </button>
            </li>
          ))}
        </ul>
        {laptopsFiltradas.length === 0 && <p>No hay laptops disponibles.</p>}
      </div>

      <div className="items-list">
        <h2>📖 Mis Préstamos</h2>
        <ul>
          {misPrestamos.length > 0 ? (
            misPrestamos.map(prestamo => (
              <li key={prestamo.id} className="item">
                <div className="item-info">
                  <strong>{prestamo.titulo || prestamo.marca}</strong> - {prestamo.autor || prestamo.modelo}
                  <p>📅 Inicio: {prestamo.fecha_inicio} | 📅 Fin: {prestamo.fecha_fin}</p>
                </div>
              </li>
            ))
          ) : (
            <p>No tienes préstamos activos.</p>
          )}
        </ul>
      </div>
    </div>
  );
}

export default HomeProfesor;
