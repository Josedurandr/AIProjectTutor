import React, { useState } from "react";
import "./LoginForm.css";
import { Link, useNavigate } from "react-router-dom"; // Importa useNavigate
import axios from "axios";

const LoginForm: React.FC = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate(); // Agrega esta línea para usar el hook useNavigate

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    console.log("Email:", email);
    console.log("Password:", password);

    try {
      // Realiza una solicitud POST con Axios
      const response = await axios.post("RUTA AQUI", {
        email,
        password,
      });

      console.log(response.data);

      if (response.data.authenticated) {
        // Asegúrate de cambiar esto según la estructura de tu respuesta
        navigate("/ChatPage"); // Redirige al usuario a la página de chat
      }
    } catch (error) {
      console.error("Hubo un error al iniciar sesión:", error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <div>
        <label htmlFor="email"></label>
        <input
          className="email"
          type="text"
          id="email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          placeholder="Email"
        />
      </div>
      <div>
        <label htmlFor="password"></label>
        <input
          className="password"
          type="password"
          id="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          placeholder="Password"
        />
        <div className="ForgotPassword">
          <a>Forgot Password?</a>
        </div>
      </div>
      <button className="signIn" type="submit">
        Sign in
      </button>
      <div className="SingUp">
        <p className="dontAcc">Dont have an account? </p>
      </div>
    </form>
  );
};

export default LoginForm;
