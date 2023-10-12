import React, { useState } from "react";
import "./LoginForm.css";
import { Link } from "react-router-dom";
import axios from "axios"; // Importa Axios

const LoginForm: React.FC = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    console.log("Username:", username);
    console.log("Password:", password);

    try {
      // Realiza una solicitud POST con Axios
      const response = await axios.post("RUTA AQUI", {
        username,
        password,
      });

      console.log(response.data); // Imprime la respuesta en la consola
    } catch (error) {
      console.error("Hubo un error al iniciar sesión:", error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <div>
        <label htmlFor="username"></label>
        <input
          className="username"
          type="text"
          id="username"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
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
        <p className="dontAcc">
          Dont have an account?{" "}
          <Link to="/SignUpPage" className="signUp">
            Sign Up
          </Link>
        </p>
      </div>
      <Link to="/ChatPage" className="linkchat">
        Ir al Chat
      </Link>
    </form>
  );
};

export default LoginForm;
