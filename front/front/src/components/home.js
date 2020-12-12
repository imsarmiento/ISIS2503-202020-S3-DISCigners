import React from 'react';
import monitor from '../static/media/monitor.jpg'; 

function Home(props) {
    return (
    <div className="container" id="minH580">
        <div id="header" className="login-box auth0-box before">
          <img id="monitor" src={monitor} />
        </div>
    </div>
    );
}

export default Home;