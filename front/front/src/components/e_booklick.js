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

    const prueba = () => {
        try {
            const res = await fetch("http://54.210.118.93:8000/usuarios");
            objeto = await res.json();
            console.log(objeto)
          } finally {
            console.log("error")
        }
    };

    const prueba2 = () => {
        try {
            const res = await fetch("http://54.210.118.93:8000/contenido");
            objeto = await res.json();
            console.log(objeto)
          } finally {
            console.log("error")
        }
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
                    <button type="button" className="btn btn-success waves-effect waves-light"
                        onClick={prueba} id="textCenter">Prueba
                    </button>
                    <button type="button" className="btn btn-success waves-effect waves-light"
                        onClick={prueba2} id="textCenter">Prueba2
                    </button>
                </div>
            </div>
        </div>
        <br></br>
    </div>
    );
}

export default E_booklick;