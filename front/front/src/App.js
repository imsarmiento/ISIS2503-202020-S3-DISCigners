import './App.css';
import Navbar from './components/navbar'
import Footer from './components/footer'
import Home from "./components/home"
import E_booklick from "./components/e_booklick"
import E_universidades from "./components/e_universidades"
import Unuser from "./components/unuser"
import {Switch, Route } from "react-router-dom";

 
function App() {
  /* 
  const { isLoading } = useAuth0();

  if (isLoading) {
    return <Loading />;
  }
   */
  return (
    <>
        <br></br>
        <Navbar></Navbar>
          <Switch>
              <Route
                path="/" exact 
                component={Home}
                />
              <Route
                path="/booklick/"
                component={E_booklick}
              />
              <Route
                path="/universidades/"
                component={E_universidades}
              />
              <Route
                path="/unuser/"
                component={Unuser}
              />
          </Switch>
        <Footer></Footer>
  </>
  );
}
export default App;
