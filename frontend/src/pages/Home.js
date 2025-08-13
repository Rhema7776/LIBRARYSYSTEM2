import { Link } from "react-router-dom";

function Home() {
  return (
    <div style={{ textAlign: "center", padding: "20px" }}>
      <h1>📚 Library Management System</h1>
      <p>Welcome! Choose an action below:</p>
      <div style={{ marginTop: "20px" }}>
        <Link to="/books" style={{ marginRight: "15px" }}>View Books</Link>
        <Link to="/add-book">Add New Book</Link>
      </div>
    </div>
  );
}

export default Home;
