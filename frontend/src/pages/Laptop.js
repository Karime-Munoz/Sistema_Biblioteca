import React, { useEffect, useState } from "react";
import "../styles/Laptop.css";

function Laptop() {
  const [laptops, setLaptops] = useState([]);
  const [error, setError] = useState("");

  useEffect(() => {
    fetch("http://127.0.0.1:8000/laptops")
      .then(response => response.json())
      .then(data => {
        console.log("Laptops recibidas:", data);
        if (Array.isArray(data)) {
          setLaptops(data);
        } else {
          setError("⚠️ No se pudo cargar la lista de laptops.");
          setLaptops([]);
        }
      })
      .catch(error => {
        console.error("❌ Error cargando laptops:", error);
        setError("❌ No se pudieron cargar las laptops.");
      });
  }, []);

  return (
    <div className="laptop-container">
      <h1>Laptops Disponibles</h1>
      {error && <p className="error-message">{error}</p>}

      <div className="laptop-list">
        {laptops.length === 0 ? (
          <p className="no-laptops">No hay laptops disponibles</p>
        ) : (
          <ul>
            {laptops.map((laptop) => (
              <li key={laptop.id} className="laptop-item">
                <span className="laptop-info">
                  <strong>{laptop.marca}</strong> - {laptop.modelo} ({laptop.estado})
                </span>
                <button className="btn-prestamo">Solicitar</button>
              </li>
            ))}
          </ul>
        )}
      </div>
    </div>
  );
}

export default Laptop;
