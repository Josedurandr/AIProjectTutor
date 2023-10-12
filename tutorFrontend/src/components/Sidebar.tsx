import React from "react";
import { Progress } from "@/components/ui/progress";
import "./Sidebar.css";

const Sidebar: React.FC = () => {
  return (
    <div className="sidebar-container">
      <select className="combobox" defaultValue="">
        <option value="" disabled>
          Selecciona una opción
        </option>
        <option value="opcion1">Opción 1</option>
        <option value="opcion2">Opción 2</option>
        {/* Agrega más opciones según sea necesario */}
      </select>

      <select className="combobox" defaultValue="">
        <option value="" disabled>
          Selecciona una opción
        </option>
        <option value="opcion1">Opción 1</option>
        <option value="opcion2">Opción 2</option>
        {/* Agrega más opciones según sea necesario */}
      </select>

      <Progress value={33} />

      <button className="sign-out-button" onClick={() => alert("Signed Out!")}>
        Sign Out
      </button>
    </div>
  );
};

export default Sidebar;
