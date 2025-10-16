# Q-Corp GIS Training Program

## Qanirtuuq River Monitoring & Community GIS Capacity Building

[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)
[![NSF Award](https://img.shields.io/badge/NSF-2527256-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2527256)

## About This Project

This repository contains training materials, workflows, and resources developed through a partnership between the University of Arkansas, Nalaquq LLC, and the Yup'ik community of Quinhagak, Alaska. The project integrates Western scientific methods with Yup'ik traditional knowledge to monitor the Qanirtuuq River and support community-led decision-making on critical issues including:

- **River avulsion and migration monitoring** to assess village relocation needs
- **Erosion and infrastructure impact assessment**
- **Salmon ecosystem health monitoring**
- **Disaster response and recovery mapping** (October 2025 typhoon damage assessment)

**Project Team:**
- **Nalaquq LLC** (Sean Gleason, Lynn Marie Church, Warren Jones)
- **University of Arkansas Center for Advanced Spatial Technologies (CAST)** (Jonathan Lim)
- **Qanirtuuq Incorporated** (Community partners)

**Funding:** NSF CIVIC Award #2527256 - "Dynamic Modeling of River Ecosystem Stability"

---

## Repository Structure

```
├── modules/                    # Training modules organized by topic
│   ├── 01-arcgis-online-basics/
│   ├── 02-field-data-collection/
│   ├── 03-digitizing-paper-maps/
│   ├── 04-spatial-analysis/
│   ├── 05-cartography/
│   ├── 06-remote-sensing-satellite/
│   ├── 07-remote-sensing-drones/
│   ├── 08-change-detection/
│   └── 09-river-monitoring/
├── case-studies/              # Real-world applications
│   └── typhoon-damage-2025/
├── resources/                 # Reference materials and links
├── workflows/                 # Step-by-step GIS workflows
├── scripts/                   # Python scripts and Model Builder tools
├── data-samples/             # Example datasets (where permissible)
├── videos/                   # Video tutorial links and transcripts
└── docs/                     # Additional documentation
```

---

## Training Modules

### Foundational Modules (November 2025)

1. **[ArcGIS Online Basics](./modules/01-arcgis-online-basics/)** - User registration, dashboards, Story Maps, web maps
2. **[Field Data Collection](./modules/02-field-data-collection/)** - Survey123, Field Maps, offline workflows, GNSS integration
3. **[Digitizing Paper Maps](./modules/03-digitizing-paper-maps/)** - Georeferencing, raster vs vector data
4. **[Spatial Analysis](./modules/04-spatial-analysis/)** - Geoprocessing tools, buffers, clip operations
5. **[Cartography](./modules/05-cartography/)** - Map design, coordinate systems, printing and web publishing
6. **[Remote Sensing: Satellite](./modules/06-remote-sensing-satellite/)** - Landsat, Sentinel, Wayback imagery
7. **[Remote Sensing: Drones](./modules/07-remote-sensing-drones/)** - UAS data collection and processing

### Advanced Modules (Summer 2026)

8. **[Change Detection](./modules/08-change-detection/)** - Temporal analysis of landscape change
9. **[River Monitoring](./modules/09-river-monitoring/)** - River migration, avulsion prediction, salmon mapping

---

## Case Studies

### [October 2025 Typhoon Damage Assessment](./case-studies/typhoon-damage-2025/)

Community-led damage mapping following the October 2025 typhoon that impacted Western Alaska coastal communities. This case study demonstrates:
- Mobile damage survey design
- Offline field data collection
- Community-facing recovery mapping
- Integration with emergency response partners

---

## Quick Start

### For Trainees

1. **Prerequisites:** ArcGIS Online account (Creator or Field Worker license)
2. **Start here:** [Module 1: ArcGIS Online Basics](./modules/01-arcgis-online-basics/)
3. **Need help?** Check the [Resources](./resources/) section for tutorials and troubleshooting

### For Instructors

1. Review the [Training Schedule](./docs/training-schedule.md)
2. Access [Instructor Notes](./docs/instructor-notes.md) for each module
3. Download [Assessment Materials](./docs/assessments/)

---

## Learning Objectives

By completing this training program, participants will be able to:

- **Administer** an organizational ArcGIS Online account
- **Collect** geotagged field data with Survey123 and Field Maps
- **Digitize** and georeference paper maps
- **Process** satellite and drone imagery
- **Analyze** spatial relationships and distances
- **Create** publication-quality maps and interactive web maps
- **Automate** repetitive tasks with Python and Model Builder
- **Monitor** river movement and ecosystem change over time

---

## Tools & Software

This training uses the ESRI ArcGIS platform:

- **ArcGIS Online** - Cloud-based mapping and data management
- **ArcGIS Pro** - Desktop GIS software for advanced analysis
- **ArcGIS Field Maps** - Mobile data collection
- **Survey123** - Custom survey design and deployment
- **ArcGIS Dashboards** - Real-time data visualization
- **ArcGIS StoryMaps** - Narrative web mapping
- **ArcGIS Flight** (formerly Site Scan) - Drone data processing

**Hardware:**
- Emlid Reach RS3 GNSS receiver
- DJI drones (various models)
- Starlink Roam kits for field connectivity

---

## Contributing

This is a living repository that grows with the community's needs. If you're part of the project team:

1. Fork this repository
2. Create a feature branch (`git checkout -b feature/new-module`)
3. Commit your changes with clear messages
4. Push to your branch (`git push origin feature/new-module`)
5. Open a Pull Request

### Content Guidelines

- Keep materials accessible for varying technical skill levels
- Include Yup'ik place names and traditional knowledge where appropriate
- Provide both written instructions and visual/video demonstrations
- Test all workflows before publishing
- Respect data sovereignty and community privacy

---

## Data & Privacy

**Important:** This repository contains educational materials and workflows only. Original geospatial data, especially data containing culturally sensitive information, traditional knowledge, or private community details, is stored separately and shared only with authorized project partners.

All data samples provided are either:
- Publicly available datasets
- Anonymized/generalized examples
- Synthetic data created for training purposes

---

## License

Training materials in this repository are licensed under [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)](https://creativecommons.org/licenses/by-nc-sa/4.0/).

Code and scripts are licensed under the [MIT License](./LICENSE-MIT).

---

## Acknowledgments

This project is made possible through NSF CIVIC Award #2527256 and represents a collaboration between:

- The Yup'ik community of Quinhagak, Alaska
- Qanirtuuq Incorporated
- Nalaquq LLC
- University of Arkansas Center for Advanced Spatial Technologies

**Quyana** (Thank you) to the culture bearers, elders, and community members who contribute their knowledge and time to this project.

---

## Contact

**Project Leadership:**
- **Sean Gleason** (Nalaquq LLC) - Technical Lead & Training
- **Lynn Marie Church** (Nalaquq LLC) - Project Coordination
- **Jonathan Lim** (University of Arkansas) - Curriculum Design

**Community Partners:**
- **Warren Jones** - Community Liaison & Workforce Development

For questions about this training program or collaboration opportunities, please open an issue in this repository or contact the project team through Nalaquq LLC.

---

## Related Repositories

- [River Monitoring Workflows](https://github.com/Nalaquq/river-monitoring) *(placeholder)*
- [Salmon Ecosystem Analysis](https://github.com/Nalaquq/salmon-ecosystem) *(placeholder)*
- [ArcGIS Python Tools](https://github.com/Nalaquq/arcgis-tools) *(placeholder)*

---

**Last Updated:** October 2025  
**Repository Maintainer:** Nalaquq LLC Training Team