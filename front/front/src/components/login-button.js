import React from "react";
import { useAuth0 } from "@auth0/auth0-react";

const LoginButton = () => {
  const { loginWithRedirect } = useAuth0();
  return (
    <div>
      <ul className="nav navbar-nav navbar-right">
          <li><a id="font_padding" className="navbar-link" onClick={() => loginWithRedirect()}>Login</a></li>
      </ul>
    </div>
  );
  
};
export default LoginButton;
