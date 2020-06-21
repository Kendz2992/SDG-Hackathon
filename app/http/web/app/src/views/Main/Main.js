import React, { useEffect, useState } from "react";
import {
  Container,
  Row,
  Col,
  Card,
  CardBody,
  CardHeader,
  CardTitle,
  ButtonGroup,
  Button,
} from "reactstrap";

import EventMap from "./EventMap";
import EventIcon from "../../components/EventIcon";
import "../../App.css";
import * as mockData from "../../data/skateboard-parks.json";

export default function Main() {
  const [activeEvent, setActiveEvent] = useState(null);
  const [eventData, setEventData] = useState(null);
  useEffect(() => {
    // fetch("/events")
    //   .then((res) => res.text()) // convert to plain text
    //   .then((text) => {
    //     const jlog = JSON.parse(text);
    //     // console.log(mockData);
    //     let GeoJSON = {
    //       type: "FeatureCollection",
    //       crs: {
    //         type: "name",
    //         properties: {
    //           name: "urn:ogc:def:crs:OGC:1.3:CRS84",
    //         },
    //       },
    //       features: mockData.default.features.map((feature) => {
    //         let hours = new Date().getHours();
    //         let minutes = "0" + new Date().getMinutes();
    //         let time = hours + ":" + minutes.substr(-2);
    //         feature = {
    //           ...feature,
    //           properties: {
    //             ...feature.properties,
    //             TIME: time,
    //           },
    //         };
    //         return feature;
    //       }),
    //     };
    //     setEventData(jlog);
    //   });
    const interval = setInterval(() => {
      fetch("/events/latest")
        .then((res) => res.text()) // convert to plain text
        .then((text) => {
          const jlog = JSON.parse(text);
          // console.log(mockData);
          let GeoJSON = {
            type: "FeatureCollection",
            crs: {
              type: "name",
              properties: {
                name: "urn:ogc:def:crs:OGC:1.3:CRS84",
              },
            },
            features: mockData.default.features.map((feature) => {
              let hours = new Date().getHours();
              let minutes = "0" + new Date().getMinutes();
              let time = hours + ":" + minutes.substr(-2);
              feature = {
                ...feature,
                properties: {
                  ...feature.properties,
                  TIME: time,
                },
              };
              return feature;
            }),
          };
          setEventData(jlog);
        });
    }, 2000);
    return () => clearInterval(interval);
  }, []);
  // []);

  let activeEventIconName = "";
  let popupTitle = "";
  switch (activeEvent?.type) {
    case "fire":
      activeEventIconName = "whatshot";
      popupTitle = "Fire";
      break;
    case "electric":
      activeEventIconName = "power_off";
      popupTitle = "Power outage";
      break;

    default:
      break;
  }
  return (
    <>
      <Container>
        <EventMap
          eventData={eventData}
          setActiveEvent={setActiveEvent}
          activeEvent={activeEvent}
          activeEventIconName={activeEventIconName}
          popupTitle={popupTitle}
        />
      </Container>
      <div className="events-list-container">
        <Row>
          <Col>
            <Card className="events-list-card">
              <CardHeader>
                <CardTitle tag="h2">
                  Sensor Events (
                  {
                    eventData?.events.filter((event) => event.type)
                      .length
                  }
                  )
                </CardTitle>
                {/* <ButtonGroup>
                  <Button>
                    Fire (
                    {
                      eventData?.features.filter(
                        (event) => event.properties.TYPE === "fire"
                      ).length
                    }
                    )
                  </Button>
                  <Button
                    onClick={() => {
                      let filteredData = eventData?.features.filter(
                        (event) => event.properties.TYPE === "electric"
                      );
                      setEventData({ ...eventData, features: filteredData });
                    }}
                  >
                    Power Outage (
                    {
                      eventData?.features.filter(
                        (event) => event.properties.TYPE === "electric"
                      ).length
                    }
                    )
                  </Button>
                </ButtonGroup> */}
              </CardHeader>
              <CardBody>
                <ul className="events-list">
                  {eventData?.events.filter((event) => event.type)
                    .map((event) => {
                      let iconName = "";
                      switch (event.type) {
                        case "fire":
                          iconName = "whatshot";
                          break;
                        case "electric":
                          iconName = "power_off";
                          break;

                        default:
                          break;
                      }
                      return (
                        <li
                          key={event.location.properties.address}
                          className="events-list-item"
                          onClick={() => {
                            setActiveEvent(event);
                          }}
                        >
                          <span
                            className="event-icon-wrapper"
                            style={{ marginLeft: 10 }}
                          >
                            <EventIcon
                              iconName={iconName}
                              eventType={event.type}
                              style={{ marginLeft: 3 }}
                            />
                          </span>
                          {event.location.properties.address}
                        </li>
                      );
                    })}
                </ul>
              </CardBody>
            </Card>
          </Col>
        </Row>
      </div>
    </>
  );
}
