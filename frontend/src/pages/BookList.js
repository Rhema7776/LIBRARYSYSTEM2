import React, { useEffect, useState } from "react";
import api from "../api/axios";

function BookList() {
  const [books, setBooks] = useState([]);

  useEffect(() => {
    api.get("/api/books/") // No need to pass headers manually
      .then((res) => {
        setBooks(res.data);
      })
      .catch((err) => {
        console.error("Error fetching books:", err);
      });
  }, []);

  return (
    <div>
      <h1>Book List</h1>
      <ul>
        {books.map((book) => (
          <li key={book.id}>{book.title}</li>
        ))}
      </ul>
    </div>
  );
}

export default BookList;
