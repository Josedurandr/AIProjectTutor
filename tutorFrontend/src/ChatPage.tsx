import "./ChatPage.css";
import Chat from "./components/ChatBot";
import Sidebar from "./components/Sidebar";
// import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";

function ChatPage() {
  return (
    <div className="Chat">
      <Chat />
      <div className="Sidebar">
        <Sidebar />
      </div>
    </div>
  );
}

export default ChatPage;
