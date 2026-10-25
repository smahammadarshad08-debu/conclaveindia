# Changelog

All notable changes to the **AccessMap India** project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.5.0] - 2026-10-25

### Added
- **Turn-by-Turn Live Navigation Mode**: Interactive Google Maps-style navigation HUD with top maneuver instruction card, distance indicator, and bottom route dock.
- **Spoken Audio Guidance**: Web Speech Synthesis voice assistant that announces journey start, upcoming turn directions, and distance.
- **Route Header Navigation Badge**: Added responsive arrow icon badge beside `Accessible Route Guidance` without layout shifting.
- **Voice Mute & Replay Controls**: One-tap toggle for muting voice prompts and repeating current turn instructions.
- **Animated Map Puck**: Pulsing Leaflet GPS marker highlighting active step coordinates during navigation.

---

## [1.4.0] - 2026-10-25

### Added
- **Automatic Route Page Redirection**: Seamlessly transitions the bottom sheet to the `Route` tab upon calculating an accessible path.
- **High-Accuracy Geolocation**: Added GPS location tracker and floating quick-navigation button (`#nav-my-location`).

---

## [1.3.0] - 2026-10-24

### Fixed
- Fixed layer toggle switch crashes and restored smooth Map/List tab toggles.
- Eliminated white screen blanking on layer filtering.

---

## [1.2.0] - 2026-10-24

### Added
- Mobile-first bottom sheet interface with touch swipe gestures.
- Three discrete snap stops: Peek (110px), Half-Sheet (48vh), and Full-Sheet (88vh).

---

## [1.0.0] - 2026-10-23

### Added
- Initial release of AccessMap India platform.
- Integration with OpenStreetMap and OSRM routing engine.
- MoHUA HG-2021 wheelchair and visual impairment routing criteria.
