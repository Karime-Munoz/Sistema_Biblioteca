import React, { useEffect, useState } from "react";
import axios from "axios";
import "../styles/Libros.css";  

function Libros() {
  const [libros, setLibros] = useState([]);

  useEffect(() => {
    axios.get("http://127.0.0.1:8000/libros")
      .then(response => setLibros(response.data))
      .catch(error => console.error(error));
  }, []);

  return (
    <div className="libros-container">
      <h1>Lista de Libros</h1>
      <ul>
        {libros.map(libro => (
          <li key={libro.id}>{libro.titulo} - {libro.autor}</li>
        ))}
      </ul>
    </div>
  );
}

export default Libros;
