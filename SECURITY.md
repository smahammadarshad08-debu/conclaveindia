# Security Policy — AccessMap India

## Supported Versions

We provide security updates and patches for the current active release of AccessMap India.

| Version | Supported          | Security Level |
| ------- | ------------------ | -------------- |
| 1.5.x   | :white_check_mark: | Active Support |
| 1.x     | :white_check_mark: | Maintenance    |
| < 1.0   | :x:                | End of Life    |

---

## Reporting a Vulnerability

If you discover a security vulnerability or potential privacy issue in AccessMap India, please notify the maintainers responsibly:

1. **Do NOT open a public GitHub issue.**
2. Submit a private security advisory via the GitHub repository's **Security** tab (`Security > Advisories > Report a vulnerability`).
3. Include detailed steps to reproduce the issue, environment information, and any proposed mitigation.

We will acknowledge receipt within 48 hours and work with you to remediate and publish a coordinated advisory.

---

## Security Best Practices & Threat Model

1. **Data Minimization**: AccessMap India does not store user location histories or persistent personal identifiable information (PII) on central servers. Geolocation queries are evaluated client-side in the browser.
2. **Transport Layer Security**: All API traffic to OpenStreetMap, OSRM, and Nominatim is encrypted over TLS 1.3 (HTTPS).
3. **Content Security Policy**: Inline scripts are locked down, and cross-origin resource requests are restricted to validated spatial endpoints.
