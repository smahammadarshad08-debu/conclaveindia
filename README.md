<div align="center">

# ♿ AccessMap India
### High-Precision Universal Pedestrian & Step-Free Navigation System
**Compliant with the Ministry of Housing & Urban Affairs (MoHUA) Harmonised Guidelines 2021 (HG-2021)**

[![Render Status](https://img.shields.io/badge/Render-Deploy%20Ready-46E3B7?style=for-the-badge&logo=render&logoColor=white)](https://render.com)
[![Standards](https://img.shields.io/badge/Standards-MoHUA%20HG--2021-10b981?style=for-the-badge&logo=gov.uk&logoColor=white)](https://mohua.gov.in)
[![Leaflet](https://img.shields.io/badge/Map%20Engine-Leaflet%201.9.4-16a34a?style=for-the-badge&logo=leaflet&logoColor=white)](https://leafletjs.com)
[![PWA](https://img.shields.io/badge/PWA-Offline%20Ready-6366f1?style=for-the-badge&logo=pwa&logoColor=white)](#-offline-first--pwa-resilience)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Web%20%7C%20Mobile%20PWA-0284c7?style=for-the-badge)](#-mobile-first-app-interface)

<p align="center">
  <a href="#-key-features">Key Features</a> •
  <a href="#-system-architecture">System Architecture</a> •
  <a href="#-routing-logic--algorithm">Routing Algorithm</a> •
  <a href="#-render-cloud-deployment-guide">Render Deployment</a> •
  <a href="#-mohua-hg-2021-compliance-matrix">HG-2021 Standards</a> •
  <a href="#-local-development">Local Setup</a>
</p>

---

</div>

## 📌 Executive Overview

**AccessMap India** is an open-source, mobile-first pedestrian navigation and spatial accessibility auditing platform engineered specifically for Indian urban contexts, healthcare facilities, and transit interchanges (featuring high-density precincts like the **AIIMS New Delhi Metro & Hospital Precinct**).

Unlike conventional navigation engines that optimize solely for vehicular travel or distance, AccessMap computes pedestrian journeys constrained by physical topography, stairs, ramp gradients, surface smoothness, dropped kerb vertical lips, tactile paving continuity, and real-time community-reported obstacles.

```
       Conventional Navigation                       AccessMap India
 ┌──────────────────────────────────┐      ┌──────────────────────────────────┐
 │  Distance: 320m                  │      │  Distance: 410m (Step-Free)      │
 │  Route: Direct flight of stairs  │  VS  │  Route: Continuous ramp & skywalk│
 │  ❌ Wheelchair: IMPASSIBLE       │      │  ✓ Wheelchair: 100% ACCESSIBLE   │
 │  ❌ Vision-Impaired: DANGEROUS   │      │  ✓ TGSI Tactile: FULL GUIDANCE   │
 └──────────────────────────────────┘      └──────────────────────────────────┘
```

---

## 🏗️ System Architecture

The application is structured into four cohesive layers, ensuring zero external framework overhead, instantaneous 0-second deployment builds, and pure client-side resilience.

```mermaid
flowchart TD
    subgraph Presentation["1. Presentation & Mobile Interface"]
        UI_Map["Full-Bleed Leaflet 1.9.4 GIS Map"]
        UI_Sheet["Sliding Bottom Sheet Drawer"]
        UI_Pill["Floating Search & Precinct Pill"]
        UI_Locate["Crosshairs Real-Time Geolocation"]
    end

    subgraph Controller["2. Controller & State Layer"]
        L_Toggle["Layer Visibility Controller\n(Steps, Ramps, Crossings, Tactile, Places, Reports)"]
        Insp["HG-2021 Inspector Modal"]
        Geo_Engine["High-Accuracy GPS & WatchPosition Tracker"]
        Mod_Desk["Auditor & Citizen Moderation Desk"]
    end

    subgraph Engine["3. Routing & Spatial Graph Engine"]
        Graph_Build["Spatial Adjacency Graph\n(Nodes, Edges, Slopes, Widths)"]
        Router["Multi-Profile Dijkstra / A* Routing Engine"]
        Barrier_Cost["Dynamic Barrier Avoidance Penalty Matrix"]
    end

    subgraph Storage["4. Data, Ingestion & Offline Resilience"]
        Precinct_Data["Curated High-Res Precinct Topology"]
        Overpass_API["Live OpenStreetMap Overpass API"]
        Local_Store["LocalStorage (Audits, Barriers, Offline Cache)"]
        PWA_Worker["Service Worker & Offline Fallback Vector SVG"]
    end

    Presentation <--> Controller
    Controller <--> Engine
    Engine <--> Storage
    Presentation <--> Storage
```

---

## 🚀 Key Features

### 📱 Mobile-First App Interface
* **Dual Viewport Layout:** Full-bleed Leaflet interactive map at the top with an ergonomic draggable sliding bottom sheet drawer at the bottom.
* **Seamless View Modes:** Instant toggle between **Map Focus** (auto-collapsing the bottom drawer) and **List Focus** (expanding verified infrastructure rows).
* **Scroll Lock Protection:** Zero-shift viewport locks prevent iOS/Android viewport displacement or blank white voids during keyboard focus or switch toggling.

### 🎛️ Dynamic 6-Category Infrastructure Layer Controller
Audited precinct infrastructure is segregated into discrete vector layers that can be toggled on or off in real time without refreshing:
1. **Steps & Stairs:** Displays stair flights, step counts, and handrail status (`layers.steps`).
2. **Ramps & Elevators:** Highlights step-free gradient paths and lifts (`layers.ramps`).
3. **Crossings & Dropped Kerbs:** Maps pedestrian crossings with tactile blisters and flush kerbs (`layers.crossings`).
4. **Tactile Guiding Paths:** Identifies TGSI sinusoidal directional tiles (`layers.tactile`).
5. **Accessible Entrances:** Locates zero-step, wide doorways with clearance notes (`layers.places`).
6. **Community & Auditor Reports:** Real-time crowd-sourced barrier hazard pins (`layers.reports`).

### 🎯 Real-Time Geolocation Tracking & Navigation Icon
* **Crosshairs Floating Action Button:** One-tap navigation icon (`#locate-button`) to pan and zoom directly to your current location.
* **Real-Time Accuracy Ring:** Displays live GPS positioning and estimated radius circle.
* **Auto-Origin Setting:** Instantly assigns current GPS coordinates as the journey start node.

### 🧭 Multi-Profile Pedestrian Routing Engine (A*)
Four specialized routing modes tailored to distinct mobility profiles:
* **♿ Step-Free (Wheelchair / Pram):** Hard cutoff on stairs ($cost = \infty$), strictly enforces slopes $\le 8.33\%$ (1:12), penalizes uneven paving, and routes via elevators and ramps.
* **🦯 Tactile / Vision:** Prioritizes continuous tactile ground surface indicators (TGSI), avoids unprotected elevation drops, and favors crossings with acoustic signals.
* **🚶 Easy Walk:** Minimizes elevation changes and steep climbs for senior citizens and persons with heart conditions.
* **⚡ Standard Pedestrian:** Pure Euclidean distance optimization for unconstrained pedestrians.

### 🛡️ MoHUA HG-2021 Standards Inspector
* Direct modal inspection of any mapped feature against specific clauses of the **Harmonised Guidelines and Standards for Universal Accessibility in India (2021)**.
* Evaluates physical dimensions: ramp slope gradient, handrail height, tactile warning placement, and doorway clear openings.

### 📋 Citizen Barrier Auditing & Moderation Desk
* **In-the-Field Reporting:** Citizens can report broken kerbs, construction obstructions, or parked vehicles with severity levels: *Passable*, *Restricted*, or *Blocked*.
* **Auditor Verification:** Certified auditors can verify, resolve, or reject reports.
* **Data Portability:** 1-click export of audited precinct data to standard **GeoJSON** and **CSV**.

---

## 🧮 Routing Logic & Penalty Cost Matrix

```mermaid
flowchart TD
    Start([User Requests Route]) --> Input[Read Start & End Coordinates]
    Input --> FindNodes[Locate Nearest Graph Nodes in Precinct]
    FindNodes --> SelectMode{Active Routing Profile}

    SelectMode -->|Step-Free| Wheelchair[Apply HG-2021 Wheelchair Penalties]
    SelectMode -->|Tactile/Vision| Tactile[Apply TGSI Guiding & Acoustic Preferences]
    SelectMode -->|Easy Walk| Easy[Apply Slope & Step Count Penalties]
    SelectMode -->|Standard| Standard[Pure Distance Cost]

    Wheelchair --> CheckStairs{Edge Has Steps?}
    CheckStairs -->|Yes| BlockEdge[Edge Cost = Infinity]
    CheckStairs -->|No| CheckSlope{Slope > 8.3%?}
    CheckSlope -->|Yes| SlopePenalty[Edge Cost += Slope Delta * 1500]
    CheckSlope -->|No| CheckRamp{Is Ramp / Lift?}
    CheckRamp -->|Yes| RampBonus[Edge Cost *= 0.85 Bonus]
    CheckRamp -->|No| BarrierCheck

    Tactile --> CheckTGSI{Has Tactile Tiles?}
    CheckTGSI -->|Yes| TGSIBonus[Edge Cost *= 0.50 Bonus]
    CheckTGSI -->|No| BarrierCheck

    Easy --> EasyStepCalc[Edge Cost += Steps * 20 + Slope * 2.5]
    EasyStepCalc --> BarrierCheck
    SlopePenalty --> BarrierCheck
    RampBonus --> BarrierCheck
    Standard --> BarrierCheck

    BarrierCheck{Active Reported Barrier On Edge?}
    BarrierCheck -->|Yes & Avoid Active| BlockEdge
    BarrierCheck -->|No| Dijkstra[Execute Dijkstra / A* Shortest Path]
    BlockEdge --> Dijkstra

    Dijkstra --> RouteFound{Route Exists?}
    RouteFound -->|Yes| RenderRoute[Render High-Contrast Polyline & Step Directions]
    RouteFound -->|No| DetourWarning[Display 'No Step-Free Path' Alert & Alternative]
```

---

## 🔄 Citizen Auditing & Moderation Lifecycle

```mermaid
sequenceDiagram
    autonumber
    actor Citizen as Citizen / Commuter
    participant UI as Mobile PWA Interface
    participant Local as LocalStorage State
    actor Auditor as Accessibility Auditor
    participant Desk as Moderation Desk
    participant Map as Leaflet Layer Group

    Citizen->>UI: Pinpoints Barrier on Map (e.g. Broken Dropped Kerb)
    Citizen->>UI: Selects Severity (Blocked / Restricted) & Notes
    UI->>Local: Persists new Report record
    UI->>Map: Plots Warning Pip Marker (Status: PENDING)
    
    Auditor->>Desk: Opens Moderation Desk Panel
    Desk->>Local: Queries Pending Citizen Reports
    Auditor->>Desk: Reviews Field Dimensions against HG-2021
    Auditor->>Desk: Clicks 'Verify' or 'Resolve'
    Desk->>Local: Updates moderationState = 'verified'
    Desk->>Map: Updates Marker Color (Green Checked Pip)
    Desk->>UI: Refreshes Category Badges & Routing Engine Invalidation
```

---

## 📐 MoHUA HG-2021 Compliance Matrix

The system validates urban infrastructure against the **Harmonised Guidelines and Standards for Universal Accessibility in India (2021)** published by the Ministry of Housing and Urban Affairs (MoHUA):

| Infrastructure Element | MoHUA HG-2021 Clause | Mandatory Indian Standard | AccessMap Enforcement |
| :--- | :--- | :--- | :--- |
| **Pedestrian Walkway Width** | § 4.1 | $\ge 1200\text{ mm}$ (clear continuous), $1800\text{ mm}$ for passing | Enforced in path cost calculation; flags edges $< 1.2\text{m}$. |
| **Ramp Gradient** | § 4.3 | Max $1:12$ ($8.33\%$), $1:15$ to $1:20$ preferred for long spans | Slopes $> 8.3\%$ flagged non-compliant; heavily penalized in wheelchair mode. |
| **Kerb Ramps** | § 4.2 | Flush lip with road surface ($\le 15\text{ mm}$ rounded lip) | Avoids kerb drop steps; prioritizes pelican crossings. |
| **Stairs & Steps** | § 4.4 | Riser $\le 150\text{ mm}$, Tread $\ge 300\text{ mm}$, Handrails on both sides | Strict avoidance in Step-Free mode ($cost = \infty$). |
| **Tactile Guiding (TGSI)** | § 4.5 | Sinusoidal guiding & hazard blister warning tiles | 50% routing cost discount in Vision/Tactile mode. |
| **Building Entrances** | § 5.1 | Level entrance or ramped approach, doorway width $\ge 900\text{ mm}$ | Audited entrance feature cards with door width verification. |

---

## ☁️ Render Cloud Deployment Guide

This repository is optimized for **1-click automated deployment on [Render](https://render.com)**.

### Deployment Method A: Blueprint Deployment (Recommended)
1. Fork or push this repository to your GitHub account:
   `https://github.com/smahammadarshad08-debu/conclaveindia.git`
2. Log into the **[Render Dashboard](https://dashboard.render.com/)**.
3. Click **New +** $\rightarrow$ **Blueprint**.
4. Connect your GitHub repository.
5. Render will automatically read [`render.yaml`](render.yaml) and configure:
   * **Service Name:** `accessmap-india`
   * **Runtime:** Python
   * **Build Command:** `pip install -r requirements.txt`
   * **Start Command:** `python server.py`
   * **Health Check Path:** `/healthz`
6. Click **Apply**. Your service will be live in seconds at `https://<your-app>.onrender.com`!

### Deployment Method B: Manual Web Service
If setting up manually in Render without Blueprints:
* **Environment:** `Python`
* **Region:** Any (e.g., `Oregon (US West)` or `Frankfurt (EU Central)`)
* **Branch:** `main`
* **Build Command:** `pip install -r requirements.txt` (or leave empty)
* **Start Command:** `python server.py` *(or `python start`)*
* **Environment Variables:**
  * `PORT` = `10000` *(Render sets this automatically)*
* **Health Check Path:** `/healthz`

### Deployment Method C: Render Static Site
If you prefer pure CDN hosting without a Python container:
* **Environment:** `Static`
* **Build Command:** `echo "Static build ready"`
* **Publish Directory:** `accessmap-site`

---

## 💻 Local Development

### Prerequisites
* **Python 3.9+** (Standard installation, no third-party pip packages needed)
* Any modern web browser

### Quick Launch
Clone the repository and run the built-in production server:

```bash
# 1. Clone repository
git clone https://github.com/smahammadarshad08-debu/conclaveindia.git
cd conclaveindia

# 2. Launch production web server
python server.py
```

The application will be accessible at:
```
http://localhost:10000/
```

### Windows 1-Click Launchers
For Windows users, pre-configured launcher scripts are provided:
* Double-click [`Start-AccessMap.bat`](Start-AccessMap.bat)
* Or execute in PowerShell:
  ```powershell
  .\Start-AccessMap.ps1
  ```

---

## 📂 Repository File Structure

```
conclaveindia/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.md             # Standardized bug reporting form
│   │   ├── feature_request.md        # Feature request template
│   │   └── barrier_report.md         # Field infrastructure hazard template
│   └── PULL_REQUEST_TEMPLATE.md      # PR guidelines & HG-2021 verification
├── accessmap-site/
│   ├── app.js                        # Core GIS routing, layer toggles & state
│   ├── index.html                    # Mobile-first semantic UI application
│   ├── styles.css                    # Responsive styling, sheet drawer & themes
│   ├── manifest.json                 # Web App Manifest (PWA installation)
│   ├── map-preview.svg               # Vector precinct overview graphic
│   ├── server.py                     # Local precinct server
│   ├── start                         # Local precinct unix launcher
│   ├── Start-AccessMap.bat           # Local Windows batch script
│   └── Start-AccessMap.ps1           # Local PowerShell script
├── .gitignore                        # Comprehensive Python, Node, OS ignore rules
├── CODE_OF_CONDUCT.md                # Contributor Covenant v2.1
├── CONTRIBUTING.md                   # Development & HG-2021 contribution guide
├── index.html                        # Root redirect & CDN fallback entrypoint
├── LICENSE                           # Open-source MIT License
├── Procfile                          # Heroku / PaaS process declaration
├── README.md                         # Project documentation & visual guide
├── render.yaml                       # Render Blueprint declaration (Web & Static)
├── requirements.txt                  # Python dependencies declaration (0 external)
├── SECURITY.md                       # Coordinated vulnerability disclosure policy
├── server.py                         # Production server with /healthz endpoint
├── start                             # Render executable entrypoint with shebang
├── Start-AccessMap.bat               # Root Windows launcher batch script
└── Start-AccessMap.ps1               # Root Windows PowerShell launcher script
```

---

## 📶 Offline-First & PWA Resilience

1. **Vector SVG Map Engine:** When network tile services are unreachable or direct file inspection is used, the system transparently activates an SVG vector fallback engine (`offline-svg-map`) rendering precinct geometry.
2. **PWA Manifest:** Installs as an independent native app on iOS Safari and Android Chrome via [`manifest.json`](accessmap-site/manifest.json).
3. **Local State Persistence:** Auditor verifications, custom barrier additions, and map preferences remain cached across browser sessions via `localStorage`.

---

## 🤝 Contributing

We welcome contributions from accessibility advocates, urban designers, software engineers, and civic data auditors!
Please read our [Contributing Guidelines](CONTRIBUTING.md) and [Code of Conduct](CODE_OF_CONDUCT.md) before submitting a Pull Request.

---

## 📜 Citations & Attributions

* **Harmonised Guidelines and Standards for Universal Accessibility in India (2021)**: Ministry of Housing and Urban Affairs (MoHUA), Government of India.
* **Map Data & Tiles**: &copy; [OpenStreetMap Contributors](https://www.openstreetmap.org/copyright) under ODbL.
* **Leaflet GIS Engine**: Vladimir Agafonkin & Leaflet contributors under BSD-2-Clause.

---

## ⚖️ License

Distributed under the **MIT License**. See [`LICENSE`](LICENSE) for full details.
