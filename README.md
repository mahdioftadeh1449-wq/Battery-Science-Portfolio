# Autonomous Battery Materials Informatics Lab

![Field](https://img.shields.io/badge/Domain-AI4Science%20%7C%20Computational%20Materials-darkblue)
![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Frameworks](https://img.shields.io/badge/Frameworks-PyTorch%20%7C%20Pymatgen%20%7C%20BoTorch-darkred)
![License](https://img.shields.io/badge/License-MIT-green)

An advanced computational research portfolio dedicated to the closed-loop autonomous discovery, high-throughput Density Functional Theory (DFT) calculations, and defect engineering of next-generation energy storage materials (Sodium-ion and beyond).

---

## 🎯 Research Focus & Architecture
This laboratory repository follows a modular multi-project structure designed for reproducible, publication-grade materials informatics:

### 📁 Active Projects

| Project | Sub-Directory | Description | Status |
| :--- | :--- | :--- | :--- |
| **Project 1: NASICON Cathodes** | [`project1_nasicon_defect/`](./project1_nasicon_defect) | Closed-loop discovery, doping, and defect engineering in $\text{Na}_x\text{M}_2(\text{PO}_4)_3$ frameworks using GNNs & Active Learning. | 🟡 Active |

---

## 🛠 Core Methodology & Tech Stack
- **Quantum Mechanics & DFT:** `VASP`, `pymatgen`, `ase`
- **Materials Informatics:** `mp-api`, `matminer`
- **Graph Neural Networks (Surrogate Models):** `PyTorch Geometric`, `ALIGNN`, `M3GNet` / `CGCNN`
- **Active Learning & Optimization:** `BoTorch`, `GPyTorch` (Bayesian Optimization via UCB/EI)

---

## 📂 Multi-Project Repository Structure
Battery-Science-Portfolio/

├── .env # Local API keys (excluded from VCS)

├── .gitignore # Global ignore rules for raw data and binaries

├── environment.yml # Unified Conda environment specification

├── LICENSE # MIT License

├── README.md # Main portfolio gateway (this file)

└── project1_nasicon_defect/ # Project 1: NASICON Defect Engineering

├── data/ # Project data (raw CIFs and processed graphs)

├── docs/ # Research notes, protocols, and derivations

├── figures/ # Vector plots, phase diagrams, and parity charts

├── models/ # Checkpoints and trained surrogate models

├── scripts/ # End-to-end reproducible Python pipelines

└── README.md # Project-specific technical documentation

### 2. Configure Computational Environment
Recreate the unified Conda environment containing PyTorch, Pymatgen, and all ML dependencies:

```bash
conda env create -f environment.yml
conda activate dft-ml-advanced
```

### 3. API Key Configuration
Create a `.env` file in the repository root and provide your Materials Project API key:

```bash
echo MP_API_KEY=your_materials_project_api_key_here > .env
```

### 4. Fetch Baseline Structure
Run the baseline ingestion pipeline to retrieve the pristine $\text{Na}_3\text{V}_2(\text{PO}_4)_3$ crystal structure (`mp-20371`):

```bash
python project1_nasicon_defect/scripts/fetch_baseline.py
```

## 👨‍💻 Principal Investigator

**Mahdi Oftadeh**  
* **Research Focus:** Autonomous Materials Discovery, Computational Defect Engineering, Solid-State Battery Cathodes.
* 
## 📜 License
This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
