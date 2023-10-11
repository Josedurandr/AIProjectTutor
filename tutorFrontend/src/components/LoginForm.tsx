import React, { useState } from "react";
import "./LoginForm.css";
import { Link } from "react-router-dom";

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
