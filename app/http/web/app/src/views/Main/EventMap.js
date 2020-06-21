import React, { useState } from "react";
import ReactDOMServer from "react-dom/server";
import { Map, Marker, Popup, TileLayer } from "react-leaflet";
import L from "leaflet";
import {
  Button,
  Card,
  CardHeader,
  CardTitle,
  CardBody,
  CardText,
  Row,
} from "reactstrap";

import EventIcon from "../../components/EventIcon";

export default function EventMap({
  eventData,
  setActiveEvent,
  activeEvent,
  activeEventIconName,
  popupTitle,
}) {
  return (
    <Map center={[27.7676, -82.6403]} zoom={12}>
      <TileLayer
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        attribution='&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
      />

      {eventData.features.map((event) => {
        let iconName = "";
        switch (event.properties.TYPE) {
          case "fire":
            iconName = "whatshot";
            break;
          case "electric":
            iconName = "power_off";
            break;

          default:
            break;
        }
        let IconComponent = (
          <EventIcon iconName={iconName} eventType={event.properties.TYPE} />
        );
        const icon = L.divIcon({
          className: "custom-icon",
          html: ReactDOMServer.renderToString(IconComponent),
        });
        return (
          <Marker
            key={event.properties.PARK_ID}
            position={[
              event.geometry.coordinates[1],
              event.geometry.coordinates[0],
            ]}
            onClick={() => {
              setActiveEvent(event);
            }}
            icon={icon}
          />
        );
      })}

      {activeEvent && (
        <Popup
          position={[
            activeEvent.geometry.coordinates[1],
            activeEvent.geometry.coordinates[0],
          ]}
          onClose={() => {
            setActiveEvent(null);
          }}
        >
          <Card>
            <CardHeader style={{ borderBottom: "1px solid" }}>
              <CardTitle tag="h2">
                <span className="event-icon-wrapper" style={{ marginLeft: 10 }}>
                  <EventIcon
                    iconName={activeEventIconName}
                    eventType={activeEvent.properties.TYPE}
                    style={{ marginTop: 4, marginLeft: 5, fontSize: 18 }}
                  />
                </span>
                {popupTitle || "Event"} detected!
                <Button
                  className="popup-close"
                  onClick={() => setActiveEvent(null)}
                >
                  <span className="material-icons f-s-18">close</span>
                </Button>
              </CardTitle>
            </CardHeader>
            <CardBody>
              <Row style={{ display: "flex", alignItems: "flex-end" }}>
                <span className="material-icons">location_on</span>
                <CardText className="m-b-0 p-l-5 f-s-14">
                  {activeEvent.properties.ADDRESS}
                </CardText>
              </Row>
              <Row style={{ display: "flex", alignItems: "flex-end" }}>
                <span className="material-icons">schedule</span>
                <CardText className="m-b-0 p-l-5 f-s-14">
                  {activeEvent.properties.TIME || "4:21pm"}
                </CardText>
              </Row>
            </CardBody>
          </Card>
        </Popup>
      )}
    </Map>
  );
}
