# External API Integrations Specification

AccessMap India connects to public, open-standard geospatial APIs for geocoding, multi-modal routing, and accessibility barrier extraction.

---

## 1. Open Source Routing Machine (OSRM)

### Endpoint
`https://router.project-osrm.org/route/v1/{profile}/{coordinates}`

### Parameters
- **`profile`**: `foot` (pedestrian paths, sidewalks, crossings)
- **`coordinates`**: `lon1,lat1;lon2,lat2`
- **`overview`**: `full` (polyline geometry)
- **`geometries`**: `geojson`
- **`steps`**: `true` (turn-by-turn maneuvers)

### Response Processing
The response geometry is rendered as a Leaflet GeoJSON polyline with gradient styling (teal for standard accessible sidewalks, amber for moderate slopes, emerald for dedicated transit concourses).

---

## 2. Nominatim Geocoding API

### Endpoint
`https://nominatim.openstreetmap.org/search`

### Parameters
- **`q`**: Place name or address string
- **`format`**: `json`
- **`addressdetails`**: `1`
- **`limit`**: `5`
- **`countrycodes`**: `in` (restricting search results to India)

---

## 3. Overpass API (Accessibility Data Extraction)

### Endpoint
`https://overpass-api.de/api/interpreter`

### Example Query for Wheelchair & Tactile Infrastructure
```ql
[out:json][timeout:25];
(
  node["wheelchair"="yes"](bbox);
  node["tactile_paving"="yes"](bbox);
  node["highway"="elevator"](bbox);
  way["wheelchair"="yes"](bbox);
);
out body;
>;
out skel qt;
```
