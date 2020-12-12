import React from 'react';
import logo from '../static/media/logo.png'; 
import AuthenticationButton from "./authentication-button";
import { useAuth0 } from "../react-auth0-spa";


function Navbar(props) {
    const { isAuthenticated, loginWithRedirect, logout } = useAuth0();

    return (
        <nav className="navbar navbar-expand-lg navbar-light bg-light">
            <nav className="navbar navbar-light bg-light">
                <a className="navbar-brand" href="/">
                <img src={logo} width="45" height="45" alt=""></img>
                </a>
            </nav>

          <nav className="navbar navbar-light bg-light">
              <a className="navbar-brand" href="/">
                  Booklick
              </a>
          </nav>
          <div className="collapse navbar-collapse" id="navbarSupportedContent">
            <ul className="navbar-nav mr-auto">
                <li className="nav-item">
                    <a className="nav-link" href="/booklick/">Estadísticas Booklick</a>
                </li>
                <li className="nav-item">
                    <a className="nav-link" href="/universidades/">Estadísticas Universidad</a>
                </li>
            </ul>
            <div>
                {!isAuthenticated && (
                    <button onClick={() => loginWithRedirect({})}>Log in</button>)}
                {isAuthenticated && <button onClick={() => logout()}>Log out</button>}
            </div>
            {/*}<AuthenticationButton />*/}
          </div>
        </nav>
    );
}

export default Navbar;