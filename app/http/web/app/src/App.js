import React from "react";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";

import indexRoutes from "./routes/";
import "./App.css";

export default function App() {
  return (
    <div className="App">
      <Router basename="/">
        <Switch>
          {indexRoutes.map((prop, key) => {
            return (
              <Route path={prop.path} key={key} component={prop.component} />
            );
          })}
        </Switch>
      </Router>
    </div>
  );
}
