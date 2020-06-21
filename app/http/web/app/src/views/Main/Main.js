import React, { useState, useEffect } from "react";
import EventMap from "./EventMap";
import "../../App.css";
import { Container, Row, Col } from "reactstrap";

export default function Main() {
  useEffect(() => {
    const interval = setInterval(() => {
      console.log("This will run every second!");
    }, 10000);
    return () => clearInterval(interval);
  }, []);
  return (
    <div className="App">
      <Container>
        <Row>
          <Col sm={9}>
            <div
              style={{ position: "relative", height: "100vh", width: "100%" }}
            >
              <EventMap />
            </div>
          </Col>
          <Col sm={3}>
            <div
              style={{ height: 100, width: 100, background: "dodgerblue" }}
            />
          </Col>
        </Row>
      </Container>
    </div>
  );
}
