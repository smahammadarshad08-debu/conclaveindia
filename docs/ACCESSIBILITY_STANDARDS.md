# Accessibility Standards & Legal Compliance Guidelines

AccessMap India implements the statutory requirements and design parameters outlined in:
1. **Rights of Persons with Disabilities (RPwD) Act, 2016** (Sections 40, 41, 42)
2. **MoHUA Harmonised Guidelines and Standards for Universal Accessibility in India (2021)**
3. **W3C Web Content Accessibility Guidelines (WCAG) 2.1 Level AA**

---

## 1. Physical Infrastructure Standards (MoHUA HG-2021)

| Feature | Standard Requirement | AccessMap India Implementation |
| :--- | :--- | :--- |
| **Walkway Clear Width** | Minimum $1800\text{ mm}$ for 2 wheelchairs passing; minimum $1200\text{ mm}$ in tight corridors. | Routes with clear width $< 1200\text{ mm}$ trigger warning badges. |
| **Ramp Slope (Gradient)** | Ideal $\le 1:12$ ($8.33\%$). Landings every $9\text{ m}$. | Filters out slopes $> 8.33\%$ unless the user selects "Allow Moderate Incline". |
| **Tactile Paving** | Guiding (directional lines) along continuous paths; Warning (blister dots) at curb ramps, steps, and road crossings. | Highlighting dedicated corridors with yellow dashed overlays and audio cues. |
| **Curb Ramps** | Max slope $1:12$, flared sides $\le 1:10$, flush transition ($< 6\text{ mm}$) with road surface. | Flags pedestrian crossings lacking dropped curbs or curb ramps. |
| **Elevators & Transit Lifts** | Minimum cabin size $1500\text{ mm} \times 1500\text{ mm}$, braille & audio announcements. | Prioritizes station entrances with verified elevator concourse access. |

---

## 2. Digital Accessibility Standards (WCAG 2.1 AA)

- **Color Contrast**: All primary text maintains a minimum contrast ratio of $4.5:1$ against backgrounds; large titles maintain $\ge 3:1$.
- **Focus Indicators**: 2px high-visibility outline rings on all interactive buttons, inputs, and toggle switches.
- **Screen Reader Support**: ARIA landmarks (`role="main"`, `role="region"`, `role="status"`), explicit `aria-label` attributes on icon-only buttons, and live regions (`aria-live="polite"`) for route calculation status.
- **Keyboard Navigation**: Complete tab order through origin search, destination search, routing profile pills, and live navigation controls.
