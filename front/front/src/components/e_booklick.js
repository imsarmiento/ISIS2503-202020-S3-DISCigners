import React from 'react';
import { useHistory } from "react-router-dom";


function E_booklick(props) {

    const history = useHistory();
    const proxyurl = "https://cors-anywhere.herokuapp.com/";
    // revisar mas info en https://stackoverflow.com/questions/43871637/no-access-control-allow-origin-header-is-present-on-the-requested-resource-whe

    const booklistsPromedioContenido = () => {
        history.push(`/booklick/booklistsPromedioContenido_db_get/`);
    };

    const booklistsCarrera = () => {
        history.push(`/booklick/booklistsCarrera_db_get/`);
    };

    const booklistsRango = () => {
        history.push(`/booklick/booklistsRango_db_get/`);
    };

    const getUniversidades = async () => {
        let objeto = undefined;
        try {
            const url = "http://54.210.118.93:8000/universidades"
            const res = await fetch(proxyurl + url);
            objeto = await res.json();
            console.log(objeto)
          } finally {
            console.log("error")
        }
    }; 
    const getEstudiantes = async () => {
        let objeto = undefined;
        try {
            const url = "http://54.210.118.93:8000/estudiantes"
            const res = await fetch(proxyurl + url);
            objeto = await res.json();
            console.log(objeto)
          } finally {
            console.log("error")
        }
    };

    const getContenido = async () => {
        let objeto = undefined;
        try {
            const url = "http://54.210.118.93:8000/contenidos"
            const res = await fetch(proxyurl + url);
            objeto = await res.json();
            console.log(objeto)
          } finally {
            console.log("error")
        }
    };

    const getConsultas = async () => {
        let objeto = undefined;
        try {
            const url = "http://54.210.118.93:8000/consultas"
            const res = await fetch(proxyurl + url);
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
                        onClick={getUniversidades} id="textCenter"> GET universidades
                    </button>
                    <button type="button" className="btn btn-success waves-effect waves-light"
                        onClick={getEstudiantes} id="textCenter"> GET estudiantes
                    </button>
                    <button type="button" className="btn btn-success waves-effect waves-light"
                        onClick={getContenido} id="textCenter">GET contenido
                    </button>
                    <button type="button" className="btn btn-success waves-effect waves-light"
                        onClick={getConsultas} id="textCenter">GET consultas
                    </button>
                </div>
            </div>
        </div>
        <br></br>
    </div>
    );
}

export default E_booklick;