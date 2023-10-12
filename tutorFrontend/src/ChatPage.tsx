import React from "react";
import Sidebar from "./components/Sidebar"; // Asegúrate de que la ruta sea correcta
import ChatBox from "./components/ChatBox"; //

const ChatPage: React.FC = () => {
  return (
    <div className="chat-page">
      <Sidebar />
      <ChatBox />
    </div>
  );
};

export default ChatPage;
