import React from "react";
import "./Sidebar.css";
import LinearProgress from "@mui/material/LinearProgress";
import { styled } from "@mui/system";

const CustomLinearProgress = styled(LinearProgress)({
  height: "10px",
  "& .MuiLinearProgress-bar": {
    backgroundColor: "#565656",
  },
  "& .MuiLinearProgress-barColorPrimary": {
    backgroundColor: "#20BBA9",
  },
  "& .MuiLinearProgress-dashed": {
    visibility: "hidden",
  },
});

const Sidebar: React.FC = () => {
  return (
    <div className="sidebar">
      <select className="combobox" defaultValue="">
        <option value="" disabled>
          Continente
        </option>
        <option value="opcion1">Opción 1</option>
        <option value="opcion2">Opción 2</option>
      </select>

      <select className="combobox" defaultValue="">
        <option value="" disabled>
          Pais
        </option>
        <option value="opcion1">Opción 1</option>
        <option value="opcion2">Opción 2</option>
      </select>

      <CustomLinearProgress
        className="Pbar"
        variant="buffer"
        value={20}
        valueBuffer={100}
      />

      <div>
        <button className="logOut">Log Out</button>
      </div>
    </div>
  );
};

export default Sidebar;
