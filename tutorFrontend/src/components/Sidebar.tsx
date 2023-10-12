import React from "react";
import "./Sidebar.css";
import LinearProgress from "@mui/material/LinearProgress";

const Sidebar: React.FC = () => {
  return (
    <div className="sidebar">
      <select className="combobox" defaultValue="">
        <option value="" disabled>
          Selecciona una opción
        </option>
        <option value="opcion1">Opción 1</option>
        <option value="opcion2">Opción 2</option>
      </select>

      <select className="combobox" defaultValue="">
        <option value="" disabled>
          Selecciona una opción
        </option>
        <option value="opcion1">Opción 1</option>
        <option value="opcion2">Opción 2</option>
      </select>
      <LinearProgress variant="buffer" value={44} valueBuffer={100} />
      <div>
        <button className="logOut">Log Out</button>
      </div>
    </div>
  );
};

export default Sidebar;
