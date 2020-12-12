import React from 'react';
import { useHistory } from "react-router-dom";


function E_booklick(props) {

    const history = useHistory();
    
    const booklistsPromedioContenido = () => {
        history.push(`/booklick/booklistsPromedioContenido_db_get/`);
    };

    const booklistsCarrera = () => {
        history.push(`/booklick/booklistsCarrera_db_get/`);
    };

    const booklistsRango = () => {
        history.push(`/booklick/booklistsRango_db_get/`);
    };

    return (
    <div className="content">
        <div className="">
            <div className="page-header-title">
            <h4 className="page-title" id="textCenter">Estadísticas Booklick</h4>
                <div id="textCenter" >
                    <button type="button" className="btn btn-success waves-effect waves-light"
                        onClick={booklistsPromedioContenido} id="textCenter">Contenido Promedio Booklists
                    </button>
                    <button type="button" className="btn btn-success waves-effect waves-light"
                        onClick={booklistsCarrera} id="textCenter">Booklists por carrera
                    </button>
                    <button type="button" className="btn btn-success waves-effect waves-light"
                        onClick={booklistsRango} id="textCenter">Booklists rango
                    </button>
                </div>
            </div>
        </div>
        <br></br>
    </div>
    );
}

export default E_booklick;