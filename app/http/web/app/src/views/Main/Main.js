import React, { useEffect } from "react";
import EventMap from "./EventMap";
import "../../App.css";
import { Container, Row, Col } from "reactstrap";
import * as eventData from "../../data/skateboard-parks.json";

export default function Main() {
  useEffect(() => {
    const interval = setInterval(() => {
      fetch("/testg")
        .then((res) => res.text()) // convert to plain text
        .then((text) => console.log(text));
    }, 2000);
    return () => clearInterval(interval);
  }, []);
  return (
    <Container>
      <EventMap eventData={eventData.default} />
    </Container>
  );
}
