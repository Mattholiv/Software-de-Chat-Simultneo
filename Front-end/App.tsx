import React, { useState, useEffect } from "react";

type Message = {
  username: string;
  message: string;
  time: string;
};

export default function App() {
  const [messages, setMessages] = useState<Message[]>([]);
  const [text, setText] = useState("");
  const [username, setUsername] = useState("User");

  async function loadMessages() {
    const res = await fetch("http://localhost:5000/messages");
    const data = await res.json();
    setMessages(data);
  }

  async function sendMessage() {
    if (!text) return;

    await fetch("http://localhost:5000/send", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        username,
        message: text
      })
    });

    setText("");
    loadMessages();
  }

  useEffect(() => {
    loadMessages();

    const interval = setInterval(loadMessages, 1000);
    return () => clearInterval(interval);
  }, []);

  return (
    <div className="chat">
      <h2>Chat</h2>

      <input
        placeholder="Seu nome"
        value={username}
        onChange={e => setUsername(e.target.value)}
      />

      <div className="messages">
        {messages.map((m, i) => (
          <div key={i} className="message">
            <b>{m.username}</b> ({m.time}): {m.message}
          </div>
        ))}
      </div>

      <input
        placeholder="Digite mensagem..."
        value={text}
        onChange={e => setText(e.target.value)}
        onKeyDown={e => e.key === "Enter" && sendMessage()}
      />
    </div>
  );
}