import { MapContainer, TileLayer, Marker, useMapEvents } from "react-leaflet";
import { useState } from "react";
import "leaflet/dist/leaflet.css";

function ClickHandler({ onClick }) {
  useMapEvents({
    click(e) {
      onClick(e.latlng.lat, e.latlng.lng);
    }
  });

  return null;
}

export default function WeatherMap({ onLocationSelect }) {

  const [pos, setPos] = useState([3.848, 11.502]);

  const handleClick = (lat, lng) => {
    setPos([lat, lng]);
    onLocationSelect(lat, lng);
  };

  return (
    <div className="bg-gray-900 p-4 rounded-xl mb-6">

      <h2 className="text-xl font-bold mb-3">🗺 Click Map</h2>

      <MapContainer
        center={pos}
        zoom={5}
        style={{ height: "400px", width: "100%" }}
      >

        <TileLayer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png" />

        <Marker position={pos} />

        <ClickHandler onClick={handleClick} />

      </MapContainer>

    </div>
  );
}