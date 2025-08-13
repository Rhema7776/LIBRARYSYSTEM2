import { useState } from "react";
import API from "../services/api";
import { useNavigate } from "react-router-dom";

function AddBook() {
  const [title, setTitle] = useState("");
  const [isbn, setIsbn] = useState("");
  const navigate = useNavigate();

  const handleSubmit = (e) => {
    e.preventDefault();
    API.post("/books/", { title, isbn })
      .then(() => {
        alert("Book added successfully!");
        navigate("/books");
      })
      .catch(err => {
        console.error("Error adding book:", err);
        alert("Failed to add book.");
      });
  };

  return (
    <div style={{ padding: "20px" }}>
      <h2>➕ Add a New Book</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Title:</label><br />
          <input
            type="text"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            required
          />
        </div>
        <div>
          <label>ISBN:</label><br />
          <input
            type="text"
            value={isbn}
            onChange={(e) => setIsbn(e.target.value)}
            required
          />
        </div>
        <button type="submit" style={{ marginTop: "10px" }}>
          Add Book
        </button>
      </form>
    </div>
  );
}

export default AddBook;
