import { useEffect } from "react";
import { Link } from "react-router-dom";
import "../styles/Home.css";  
import fondo from "../assets/Bibliofinal.webp";  

function Home() {
  useEffect(() => {
    document.body.style.backgroundImage = `url(${fondo})`;
    document.body.style.backgroundSize = "cover";
    document.body.style.backgroundPosition = "center";
    document.body.style.backgroundRepeat = "no-repeat";
    document.body.style.height = "100vh";
    
    return () => {
      document.body.style.backgroundImage = "";
    };
  }, []);

  return (
    <div className="home-container">
      <div className="content">
        <h1>Bienvenido a BiblioTEC</h1>
        <p>Explora nuestra colección de libros y gestiona tus préstamos.</p>
        <Link to="/login" className="btn">Acceder</Link>
      </div>
    </div>
  );
}

export default Home;
