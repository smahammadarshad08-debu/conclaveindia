# Pull Request & Contribution Checklist

Before submitting a Pull Request to **AccessMap India**, please verify the following:

- [ ] **Standards Compliance**: Does your change maintain or improve adherence to MoHUA Harmonised Guidelines 2021 and WCAG 2.1 AA?
- [ ] **Mobile Responsiveness**: Was the interface tested across phone viewports (390px, 414px) and tablet/desktop widths?
- [ ] **Keyboard & Screen Reader Accessible**: Can all interactive elements be reached and activated using keyboard tab navigation and VoiceOver/NVDA?
- [ ] **Zero Regressions**: Did all automated unit and static tests pass? (`python -m unittest discover -s tests`)
- [ ] **Clean Code**: Are variables clearly named, free of dead code, and formatted consistently with `.editorconfig`?
- [ ] **Documentation**: Are changes reflected in the `README.md`, `CHANGELOG.md`, or relevant document in `docs/`?
