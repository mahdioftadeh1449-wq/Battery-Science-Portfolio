# 🔋 Autonomous Discovery and Defect Engineering of NASICON-Type Sodium-Ion Battery Cathodes

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Materials Project API](https://img.shields.io/badge/Materials%20Project-API%20v2-orange.svg)](https://materialsproject.org/)
[![Framework-PyTorch](https://img.shields.io/badge/PyTorch-Geometric-red.svg?logo=pytorch&logoColor=white)](https://pytorch-geometric.readthedocs.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](../../LICENSE)

---

## 🔬 Computational Methodology

### 1. Defect Thermodynamics

The defect formation energy for a dopant $X$ substituting a host atom $M$ in charge state $q$ is formulated as:

$$\Delta E_f [X_M^q] = E_{\text{tot}}[X_M^q] - E_{\text{tot}}[\text{pristine}] + \mu_M - \mu_X + q(E_F + E_V + \Delta V)$$

#### 📐 Parameter Definitions:

| Symbol | Description | Evaluation Method |
| :--- | :--- | :--- |
| $E_{\text{tot}}[X_M^q]$ | Total energy of the defective supercell | DFT (VASP / Quantum ESPRESSO) |
| $E_{\text{tot}}[\text{pristine}]$ | Total energy of the pristine reference supercell | DFT Ground State Calculation |
| $\mu_i$ | Chemical potential of atomic species $i \in \{M, X\}$ | Phase boundary stability analysis |
| $q$ | Net charge state of the point defect | Integer ($q \in \mathbb{Z}$) |
| $E_F$ | Fermi energy level referenced to VBM | Scanned across band gap ($0 \le E_F \le E_g$) |
| $E_V$ | Valence Band Maximum (VBM) of the pristine system | Electronic Density of States (DOS) |
| $\Delta V$ | Electrostatic potential alignment correction | Core-level alignment method |

---

### 2. Sodium Migration Barriers

Minimum Energy Paths (MEP) and activation migration energies ($E_a$) along the three-dimensional percolating diffusion channels:

$$\text{Na}(1) \longrightarrow \text{Na}(2) \longrightarrow \text{Na}(1)$$

are modeled via the **Climbing-Image Nudged Elastic Band (CI-NEB)** method and accelerated via graph-based potential approximations.

---

## 🚀 Getting Started & Workflow

### 1. Environment Activation
Ensure the dedicated conda environment is activated:
```bash
conda activate dft-ml-advanced
### 2. Configure API Credentials
Verify that your Materials Project API key is defined in the root `.env` file:
```text
MP_API_KEY=your_materials_project_api_key_here
```

### 3. Fetch Baseline Crystal Structure
Retrieve the pristine $\text{Na}_3\text{V}_2(\text{PO}_4)_3$ unit cell (Materials Project ID: `mp-20371`):
```bash
python scripts/fetch_baseline.py
```

### 4. Defect Generation & Feature Extraction
Generate supercells with targeted vacancies and aliovalent substitutions:
```bash
python scripts/defect_generator.py --supercell 2x2x2 --dopants Ti Cr Fe
```

---

## 📊 Expected Deliverables & Milestones

- [x] Phase 1: Automated data ingestion pipeline for pristine NASICON cathodes (`mp-20371`).
- [ ] Phase 2: Parametric supercell defect library (over $10^3$ defective configurations).
- [ ] Phase 3: Trained Graph Neural Network surrogate with validation metric $R^2 > 0.92$ on formation energy.
- [ ] Phase 4: Bayesian Optimization trajectory identifying top-candidate doped structures with low migration barrier ($E_a < 0.35\text{ eV}$).

---

## 👨‍💻 Principal Investigator

**Mahdi Oftadeh**  
* **Research Focus:** Autonomous Materials Discovery, Computational Defect Engineering, Solid-State Battery Cathodes.

---

## 📜 License

This sub-project is maintained under the MIT License.
`

