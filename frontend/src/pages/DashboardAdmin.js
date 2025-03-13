import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import "../styles/DashboardAdmin.css";

function DashboardAdmin() {
  const [usuarios, setUsuarios] = useState([]);
  const [libros, setLibros] = useState([]);
  const [laptops, setLaptops] = useState([]);
  const [errorUsuarios, setErrorUsuarios] = useState("");
  const [errorLaptops, setErrorLaptops] = useState("");
  const [errorLibros, setErrorLibros] = useState("");


  const [modalVisible, setModalVisible] = useState(false);
  const [nuevoUsuario, setNuevoUsuario] = useState({
    nombre: "",
    apellido: "",
    matricula: "",
    rol: "Alumno",
    contrasena: "",
  });
  const [mensajeUsuario, setMensajeUsuario] = useState("");

  useEffect(() => {
    fetch("http://127.0.0.1:8000/usuarios")
      .then((response) => response.json())
      .then((data) => setUsuarios(Array.isArray(data) ? data : []))
      .catch(() => setErrorUsuarios("Error al conectar con el servidor."));

    fetch("http://127.0.0.1:8000/libros/todos")
      .then((response) => response.json())
      .then((data) => setLibros(Array.isArray(data) ? data : []))
      .catch(() => setErrorLibros("Error al conectar con el servidor."));

    fetch("http://127.0.0.1:8000/laptops/todos")
      .then((response) => response.json())
      .then((data) => setLaptops(Array.isArray(data) ? data : []))
      .catch(() => setErrorLaptops("Error al conectar con el servidor."));
  }, []);


  const handleInputChange = (e) => {
    setNuevoUsuario({ ...nuevoUsuario, [e.target.name]: e.target.value });
  };


  const agregarUsuario = () => {
    fetch("http://127.0.0.1:8000/usuarios", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(nuevoUsuario),
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.detail) {
          setMensajeUsuario("❌ " + data.detail);
        } else {
          setMensajeUsuario("✅ Usuario agregado correctamente");
          setUsuarios([...usuarios, nuevoUsuario]); 
          setModalVisible(false);
        }
      })
      .catch(() => setMensajeUsuario("❌ Error al conectar con el servidor."));
  };

  return (
    <div className="dashboard-admin">

      <button className="logout-button">
        <Link to="/">Cerrar Sesión</Link>
      </button>

      <h1>Panel de Administrador</h1>


      <div className="admin-buttons">
        <button className="btn-add" onClick={() => setModalVisible(true)}>
          Agregar Usuario
        </button>
        <button className="btn-add">Agregar Libro</button>
        <button className="btn-add">Agregar Laptop</button>
      </div>

      {modalVisible && (
        <div className="modal">
          <div className="modal-content">
            <h2>Agregar Usuario</h2>
            <input
              type="text"
              name="nombre"
              placeholder="Nombre"
              onChange={handleInputChange}
              required
            />
            <input
              type="text"
              name="apellido"
              placeholder="Apellido"
              onChange={handleInputChange}
              required
            />
            <input
              type="text"
              name="matricula"
              placeholder="Matrícula"
              onChange={handleInputChange}
              required
            />
            <select name="rol" onChange={handleInputChange}>
              <option value="Alumno">Alumno</option>
              <option value="Profesor">Profesor</option>
              <option value="Administrador">Administrador</option>
            </select>
            <input
              type="password"
              name="contrasena"
              placeholder="Contraseña"
              onChange={handleInputChange}
              required
            />
            {mensajeUsuario && <p>{mensajeUsuario}</p>}
            <button onClick={agregarUsuario}>Guardar</button>
            <button onClick={() => setModalVisible(false)}>Cancelar</button>
          </div>
        </div>
      )}

      {/* Sección de Usuarios */}
      <h2>Usuarios</h2>
      {errorUsuarios && <p className="error-message">{errorUsuarios}</p>}
      <div className="list-container large">
        {usuarios.length > 0 ? (
          <ul>
            {usuarios.map((usuario) => (
              <li key={usuario.matricula} className="list-item">
                {usuario.nombre} ({usuario.rol})
              </li>
            ))}
          </ul>
        ) : (
          <p>No hay usuarios registrados.</p>
        )}
      </div>

      {/* Sección de Libros */}
      <h2>📚 Libros</h2>
      {errorLibros && <p className="error-message">{errorLibros}</p>}
      <div className="list-container">
        {libros.length > 0 ? (
          <ul>
            {libros.map((libro) => (
              <li key={libro.id} className="list-item">
                {libro.titulo} - {libro.autor}
                <div className="list-actions">
                  <button
                    className={`btn-status ${
                      libro.estado === "disponible" ? "disponible" : "prestado"
                    }`}
                  >
                    {libro.estado === "disponible" ? "Disponible" : "Prestado"}
                  </button>
                  <button className="btn-edit">Editar</button>
                  <button className="btn-delete">Eliminar</button>
                </div>
              </li>
            ))}
          </ul>
        ) : (
          <p>No hay libros disponibles.</p>
        )}
      </div>

      {/* Sección de Laptops */}
      <h2>💻 Laptops</h2>
      {errorLaptops && <p className="error-message">{errorLaptops}</p>}
      <div className="list-container">
        {laptops.length > 0 ? (
          <ul>
            {laptops.map((laptop) => (
              <li key={laptop.id} className="list-item">
                {laptop.marca} - {laptop.modelo}
                <div className="list-actions">
                  <button
                    className={`btn-status ${
                      laptop.estado === "disponible" ? "disponible" : "prestado"
                    }`}
                  >
                    {laptop.estado === "disponible"
                      ? "Disponible"
                      : "Prestado"}
                  </button>
                  <button className="btn-edit">Editar</button>
                  <button className="btn-delete">Eliminar</button>
                </div>
              </li>
            ))}
          </ul>
        ) : (
          <p>No hay laptops registradas.</p>
        )}
      </div>
    </div>
  );
}

export default DashboardAdmin;
