import React from 'react';
import { useHistory } from "react-router-dom";


function E_universidades(props) {
    const history = useHistory();
    
    const basesDatos_db_get = () => {
        history.push(`/universidades/basesDatos_db_get/Universidad%20de%20los%20Andes/2020-01-01/2021-10-10/`);
    };

    const basesDatos_carreras = () => {
        history.push(`/universidades/basesDatos_carreras_db_get/Universidad%20de%20los%20Andes/2020-01-01/2021-10-10`);
    };

    return (
        <div className="content">
            <div className="">
                <div className="page-header-title">
                    <h4 className="page-title" id="textCenter">Estadísticas Universidad</h4>
                    <div id="textCenter">
                        <button type="button" className="btn btn-success waves-effect waves-light"
                            onClick={basesDatos_db_get} id="textCenter">Bases de datos universidad
                        </button>
                        <button type="button" className="btn btn-success waves-effect waves-light"
                            onClick={basesDatos_carreras} id="textCenter">Bases de datos universidad carrera
                        </button>
                    </div>
                </div>
            </div>
            <br></br>
        </div>
    );
}

export default E_universidades;