import React from "react";
import "./App.css";
import LoginForm from "./components/LoginForm";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import ChatPage from "./ChatPage";

function App() {
  return (
    <Router>
      <div className="App">
        <Routes>
          <Route path="/" element={<LoginForm />} />
          <Route path="/ChatPage" element={<ChatPage />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
