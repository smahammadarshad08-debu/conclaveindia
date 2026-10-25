#!/usr/bin/env python3
"""
Sample GeoJSON Exporter Utility for AccessMap India.
Generates compliant GeoJSON FeatureCollections for GIS analysis in QGIS / ArcGIS.
"""

import json
import os

SAMPLE_FEATURES = [
    {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [77.2185, 28.6315]
        },
        "properties": {
            "id": "landmark-connaught-place-gate-2",
            "name": "Rajiv Chowk Metro Gate 2 Elevator",
            "type": "elevator",
            "compliance": "HG-2021 Compliant",
            "tactile_paving": True,
            "clear_width_mm": 1800,
            "slope_pct": 0.0
        }
    },
    {
        "type": "Feature",
        "geometry": {
            "type": "LineString",
            "coordinates": [
                [77.2185, 28.6315],
                [77.2190, 28.6320],
                [77.2195, 28.6325]
            ]
        },
        "properties": {
            "id": "segment-inner-circle-walkway",
            "name": "Connaught Place Radial Walkway",
            "type": "tactile_corridor",
            "surface": "paved_stone",
            "tactile_guiding": True,
            "max_gradient_pct": 3.5
        }
    }
]

def export_geojson(output_file="sample_accessible_infrastructure.geojson"):
    data = {
        "type": "FeatureCollection",
        "name": "AccessMapIndia_Sample_Infrastructure",
        "crs": {
            "type": "name",
            "properties": {"name": "urn:ogc:def:crs:OGC:1.3:CRS84"}
        },
        "features": SAMPLE_FEATURES
    }
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print(f"Exported {len(SAMPLE_FEATURES)} sample features to {output_file}")

if __name__ == "__main__":
    export_geojson()
