import React, { useState } from "react";
import "./ChatBox.css";

interface Message {
  sender: "user" | "bot";
  content: string;
}

const ChatBox: React.FC = () => {
  const [messages, setMessages] = useState<Message[]>([]);
  const [input, setInput] = useState("");

  const handleSend = () => {
    if (input.trim() !== "") {
      const userMessage: Message = { sender: "user", content: input.trim() };
      setMessages((prev) => [...prev, userMessage]);

      // Aquí puedes agregar la lógica para obtener la respuesta del bot
      const botMessage: Message = {
        sender: "bot",
        content: "Hola, soy un bot.",
      };
      setMessages((prev) => [...prev, botMessage]);

      setInput("");
    }
  };

  return (
    <div className="chatbox">
      <div className="messages">
        {messages.map((message, index) => (
          <div key={index} className={`message ${message.sender}`}>
            {message.content}
          </div>
        ))}
      </div>
      <div className="input-area">
        <input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyPress={(e) => e.key === "Enter" && handleSend()}
        />
        <button onClick={handleSend}>Send</button>
      </div>
    </div>
  );
};

export default ChatBox;
