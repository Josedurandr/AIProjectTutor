import React, { useState } from "react";
import "./ChatBot.css";

interface Message {
  sender: "user" | "bot";
  content: string;
}

const ChatBot: React.FC = () => {
  const [messages, setMessages] = useState<Message[]>([]);
  const [input, setInput] = useState("");

  const handleSend = () => {
    if (input.trim() !== "") {
      setMessages([...messages, { sender: "user", content: input.trim() }]);
      setInput("");

      // Aquí puedes agregar la lógica para enviar el mensaje al backend y recibir una respuesta
      // Por ahora, solo agregaré una respuesta de bot de ejemplo
      setMessages((prev) => [
        ...prev,
        { sender: "bot", content: "conecta a backend" },
      ]);
    }
  };

  return (
    <div className="chatbot-container">
      <div className="messages-container">
        {messages.map((message, index) => (
          <div key={index} className={`message ${message.sender}`}>
            {message.content}
          </div>
        ))}
      </div>
      <div className="input-container">
        <input
          className="msg"
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Enter Text..."
        />
        <button className="send" onClick={handleSend}>
          Send
        </button>
      </div>
    </div>
  );
};

export default ChatBot;
