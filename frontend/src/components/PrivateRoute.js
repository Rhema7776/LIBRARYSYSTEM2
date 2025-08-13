// src/components/PrivateRoute.js
import React from "react";
import { Navigate } from "react-router-dom";

function PrivateRoute({ children }) {
  const token = localStorage.getItem("access_token");

  // If no token, redirect to login
  if (!token) {
    return <Navigate to="/login" />;
  }

  return children;
}

export default PrivateRoute;
