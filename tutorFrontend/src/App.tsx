import React from "react";
import "./App.css";
import LoginForm from "./components/LoginForm";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import ChatBot from "./components/ChatBot"; // Asegúrate de importar tu componente ChatBot
import Sidebar from "./components/Sidebar";

function App() {
  return (
    <Router>
      <div className="App">
        <Routes>
          <Route path="/" element={<LoginForm />} />
          <Route path="/ChatPage" element={<ChatBot />} />
        </Routes>
        <Sidebar />
      </div>
    </Router>
  );
}

export default App;
