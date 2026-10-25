#!/usr/bin/env python3
"""
Endpoint Health Checker for AccessMap India Upstream Services.
Tests connectivity to OpenStreetMap tiles, Nominatim, and OSRM routing.
"""

import urllib.request
import urllib.error
import time
import sys

ENDPOINTS = [
    ("OSRM Routing API", "https://router.project-osrm.org/route/v1/foot/77.2185,28.6315;77.2195,28.6325?overview=false"),
    ("OSM Nominatim Geocoder", "https://nominatim.openstreetmap.org/search?q=New+Delhi&format=json&limit=1"),
    ("CartoDB Positron Tile CDN", "https://a.basemaps.cartocdn.com/rastertiles/voyager/15/23315/13936.png"),
]

def check_endpoints():
    print("Checking AccessMap India upstream service endpoints...\n")
    all_ok = True
    for name, url in ENDPOINTS:
        start_time = time.time()
        try:
            req = urllib.request.Request(
                url,
                headers={"User-Agent": "AccessMapIndia-HealthCheck/1.5.0"}
            )
            with urllib.request.urlopen(req, timeout=10) as response:
                status = response.status
                elapsed = (time.time() - start_time) * 1000
                print(f"[PASS] {name:<26} -> HTTP {status} ({elapsed:.1f} ms)")
        except urllib.error.HTTPError as e:
            print(f"[WARN] {name:<26} -> HTTP {e.code}")
        except Exception as e:
            print(f"[FAIL] {name:<26} -> Error: {e}")
            all_ok = False
    return 0 if all_ok else 1

if __name__ == "__main__":
    sys.exit(check_endpoints())
