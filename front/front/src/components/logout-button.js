import React from "react";
import { useAuth0 } from "@auth0/auth0-react";

const LogoutButton = () => {
  const { logout } = useAuth0();
  return (
    <div>
      <ul class="nav navbar-nav navbar-right">
        <li><a id="font_padding" class="nav-link" onClick={() =>logout({
        returnTo: window.location.origin,})}>Log out</a></li>
      </ul>
    </div>
    
  );
};

export default LogoutButton;