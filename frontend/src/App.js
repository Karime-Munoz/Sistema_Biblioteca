import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Home from "./pages/Home";  
import Login from "./pages/Login";  
import Libros from "./pages/Libros";  
import HomeAlumno from "./pages/HomeAlumno";
import HomeProfesor from "./pages/HomeProfesor";
import DashboardAdmin from "./pages/DashboardAdmin";
import Laptop from "./pages/Laptop";

function App() {
  return (
    <Router>  
      <Routes>
        <Route path="/" element={<Home />} />  {/* Ruta principal */}
        <Route path="/login" element={<Login />} />
        <Route path="/libros" element={<Libros />} />
        <Route path="/home-alumno" element={<HomeAlumno />} />
        <Route path="/home-profesor" element={<HomeProfesor />} />
        <Route path="/dashboard-admin" element={<DashboardAdmin />} />
        <Route path="/laptops" element={<Laptop />} />
      </Routes>
    </Router>
  );
}

export default App;

