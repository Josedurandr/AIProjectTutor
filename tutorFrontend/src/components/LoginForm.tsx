import React, { useState } from "react";
import "./LoginForm.css";

const LoginForm: React.FC = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    console.log("Username:", username);
    console.log("Password:", password);
    // Aquí puedes agregar la lógica para manejar el inicio de sesión, como enviar los datos a un servidor
  };

  return (
    <form onSubmit={handleSubmit}>
      <div>
        <label htmlFor="username">Nombre de usuario</label>
        <input
          type="text"
          id="username"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
        />
      </div>
      <div>
        <label htmlFor="password">Contraseña</label>
        <input
          type="password"
          id="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
      </div>
      <button type="submit">Sign in</button>
    </form>
  );
};

export default LoginForm;
