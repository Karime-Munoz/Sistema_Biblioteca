import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import "../styles/Login.css";

function Login() {
  const [matricula, setMatricula] = useState(""); 
  const [contrasena, setContrasena] = useState("");
  const [error, setError] = useState("");
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (matricula.includes(" ") || contrasena.includes(" ")) {
      setError("No se permiten espacios en la matrícula o contraseña");
      return;
    }

    try {
      const response = await fetch("http://127.0.0.1:8000/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ matricula, contrasena }),
      });

      const data = await response.json();
      if (!response.ok) throw new Error(data.detail || "Error desconocido");

      // Esto es porque segun el rol la pag a la que se va
      if (data.rol === "Alumno") navigate("/home-alumno");
      else if (data.rol === "Profesor") navigate("/home-profesor");
      else if (data.rol === "Administrador") navigate("/dashboard-admin");
      else throw new Error("Rol no reconocido");

    } catch (error) {
      setError(error.message);
    }
  };

  return (
    <div className="login-container">
      <form className="login-form" onSubmit={handleSubmit}>
        <h2>Iniciar Sesión</h2>
        
        <input
          type="text"
          placeholder="Matrícula"
          value={matricula}
          onChange={(e) => setMatricula(e.target.value)}
          required
        />
        
        <input
          type="password"
          placeholder="Contraseña"
          value={contrasena}
          onChange={(e) => setContrasena(e.target.value)}
          required
        />
        
        {error && <p className="error-message">{error}</p>}

        <button type="submit">Ingresar</button>
      </form>
    </div>
  );
}

export default Login;
