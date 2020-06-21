import React from "react";

export default function EventIcon({ eventType, iconName, style }) {
  return (
    <div className={`${eventType}-pin`}>
      <span
        className={`material-icons event-icon ${eventType}-event`}
        style={style}
      >
        {iconName}
      </span>
    </div>
  );
}
