# Autonomous Discovery of NASICON Cathodes via Active Learning & DFT

[![Status](https://img.shields.io/badge/Status-Phase%200%3A%20Setup-blue.svg)]()
[![Python](https://img.shields.io/badge/Python-3.10%2B-green.svg)]()
[![License](https://img.shields.io/badge/License-MIT-lightgrey.svg)]()

An end-to-end framework integrating Density Functional Theory (DFT), Graph Neural Networks (GNNs), and Bayesian Optimization (Active Learning) to accelerate the discovery of high-performance, defect-tolerant NASICON-structured sodium-ion battery cathodes.

---

## 🎯 Project Objectives
1. **Accelerated Screening:** Screen composition and defect spaces in NASICON frameworks ($\text{Na}_x\text{M}_2(\text{PO}_4)_3$) with over $30\text{--}50\%$ reduction in computational cost.
2. **Defect-Aware Modeling:** Incorporate vacancy and substitution defects into surrogate machine learning models to capture realistic electrochemical responses.
3. **Closed-Loop Exploration:** Implement multi-objective Bayesian optimization balancing thermodynamic stability, average voltage, and Na-ion diffusion barriers.

---

## 🔬 Core Methodology & Tech Stack
- **Quantum Mechanics / DFT:** `VASP`, `pymatgen`, `ase`
- **Materials Informatics:** `matminer`, `mp-api`
- **Machine Learning / GNNs:** `PyTorch Geometric`, `M3GNet` / `CGCNN`
- **Active Learning:** `BoTorch`, `GPyTorch`

---

## 📁 Repository Architecture
```text
├── data/               # Raw and processed datasets (excluded from Git)
│   ├── raw/            # Initial downloaded CIF files and MP data
│   ├── processed/      # ML-ready featurized tensors / CSVs
│   └── external/       # Reference benchmark literature data
├── notebooks/          # Step-by-step exploratory analysis
├── scripts/            # Reproducible data pipelines and workflow tools
├── docs/               # Technical protocols and meeting notes
│   ├── protocols/      # Standard Operating Procedures (SOPs)
│   └── meetings/       # Research progress logs
├── figures/            # Publication-grade vector and raster figures
├── models/             # Trained surrogate ML model checkpoints
├── .gitignore          # Excluded large/sensitive files
├── environment.yml     # Conda environment specification
├── PROJECT_LOG.md      # Daily experimental and research activity log
├── DECISIONS.md        # Architectural and scientific Decision Records (ADRs)
└── README.md           # Project showcase and entry point
