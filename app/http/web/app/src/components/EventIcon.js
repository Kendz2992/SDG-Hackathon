import React from "react";

export default function EventIcon({ eventType, iconName }) {
  return (
    <div className={`${eventType}-pin`}>
      <span className={`material-icons event-icon ${eventType}-event`}>
        {iconName}
      </span>
    </div>
  );
}
