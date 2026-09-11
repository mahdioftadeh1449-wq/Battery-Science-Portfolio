# 🔋 Autonomous Discovery and Defect Engineering of NASICON-Type Sodium-Ion Battery Cathodes

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Materials Project API](https://img.shields.io/badge/Materials%20Project-API%20v2-orange.svg)](https://materialsproject.org/)
[![Framework-PyTorch](https://img.shields.io/badge/PyTorch-Geometric-red.svg)](https://pytorch-geometric.readthedocs.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

---

## 📌 Executive Summary

Sodium-ion batteries (SIBs) represent a sustainable and cost-effective alternative to lithium-ion technologies, particularly for grid-scale energy storage. Among various cathode candidates, **NASICON-type** ($\text{Na}_x\text{M}_2(\text{PO}_4)_3$) frameworks offer superior three-dimensional sodium diffusion pathways and structural stability. 

However, pristine phases often suffer from low intrinsic electronic conductivity and kinetic barriers. This project establishes an **end-to-end, closed-loop computational discovery pipeline** combining **Density Functional Theory (DFT)** ground truths, **Graph Neural Networks (GNNs)**, and **Active Learning (Bayesian Optimization)** to systematically investigate defect engineering (aliovalent doping and vacancy formation) for enhanced electrochemical performance.

---

## 🎯 Key Objectives & Research Questions

1. **Systematic Defect Generation:** Automated generation of point defects (cation/anion vacancies) and dopant substitutions ($M = \text{Ti, Cr, Fe, Mn, Zr}$) on the baseline $\text{Na}_3\text{V}_2(\text{PO}_4)_3$ crystal framework.
2. **DFT-Informed Data Foundation:** High-throughput computation of defect formation energies ($\Delta E_f$), electronic band gaps ($E_g$), and volume expansion ratios ($\Delta V / V_0$).
3. **Graph Neural Network Surrogates:** Development of crystal graph neural network models (such as CGCNN / SchNet / PaiNN) to predict migration barriers ($E_a$) and open-circuit voltages (OCV) with DFT-level precision at orders-of-magnitude lower computational cost.
4. **Active Learning Optimization:** Utilizing Gaussian Process Regression and Upper Confidence Bound (UCB) acquisition functions to navigate the multi-dimensional composition-defect space autonomously.

---

## 🏗️ Project Architecture & Directory Structure
```text
project1_nasicon_defect/
├── README.md                      # Project-specific documentation (This file)
├── scripts/                       # Executable Python modules
│   ├── fetch_baseline.py          # Automated CIF retrieval from Materials Project
│   ├── defect_generator.py        # Supercell & point-defect generator (Pymatgen)
│   ├── train_gnn.py               # Graph Neural Network training pipeline
│   └── active_learning_loop.py    # Closed-loop Bayesian acquisition engine
├── data/                          # Crystal structures & computed properties
│   ├── raw/                       # Baseline CIFs (e.g., mp-20371_Na3V2(PO4)3.cif)
│   └── processed/                 # Defect supercells & atomic feature graphs
├── models/                        # Serialized PyTorch Geometric checkpoints (.pt)
├── figures/                       # High-resolution phase diagrams & parity plots
└── docs/                          # Theoretical formulations & literature references
🔬 Computational Methodology
1. Defect Thermodynamics
The defect formation energy for a dopant 
𝑋
X
 substituting host atom 
𝑀
M
 in charge state 
𝑞
q
 is defined as:

Δ
𝐸
𝑓
[
𝑋
𝑀
𝑞
]
=
𝐸
tot
[
𝑋
𝑀
𝑞
]
−
𝐸
tot
[
pristine
]
+
𝜇
𝑀
−
𝜇
𝑋
+
𝑞
(
𝐸
𝐹
+
𝐸
𝑉
+
Δ
𝑉
)
ΔE 
f
​
 [X 
M
q
​
 ]=E 
tot
​
 [X 
M
q
​
 ]−E 
tot
​
 [pristine]+μ 
M
​
 −μ 
X
​
 +q(E 
F
​
 +E 
V
​
 +ΔV)

Where:

𝐸
tot
E 
tot
​
 
 is the supercell total energy evaluated via DFT.
𝜇
𝑖
μ 
i
​
 
 represents the chemical potential of species 
𝑖
i
.
𝐸
𝐹
E 
F
​
 
 is the Fermi energy referenced to the valence band maximum (
𝐸
𝑉
E 
V
​
 
).
2. Sodium Migration Barriers
Minimum Energy Paths (MEP) and activation energies (
𝐸
𝑎
E 
a
​
 
) along the 3D diffusion pathways (
Na1
→
Na2
→
Na1
Na1→Na2→Na1
) are modeled via the Climbing-Image Nudged Elastic Band (CI-NEB) method and accelerated via graph-based potential approximations.

🚀 Getting Started & Workflow
1. Environment Activation
Ensure the core conda environment is activated:

bash
conda activate dft-ml-advanced
2. Configure API Credentials
Make sure your Materials Project API key is set in the root .env file:

text
MP_API_KEY=your_materials_project_api_key_here
3. Fetch Baseline Crystal Structure
Retrieve the pristine 
Na
3
V
2
(
PO
4
)
3
Na 
3
​
 V 
2
​
 (PO 
4
​
 ) 
3
​
 
 unit cell (Materials Project ID: mp-20371):

bash
python scripts/fetch_baseline.py
4. Defect Generation & Feature Extraction (Next Stage)
Generate supercell structures with targeted vacancies and substitutions:

bash
python scripts/defect_generator.py --supercell 2x2x2 --dopants Ti Cr Fe
📊 Expected Deliverables
[x] Automated data ingestion pipeline for pristine NASICON cathodes.
[ ] Parametric supercell defect library (over 
10
3
10 
3
 
 defective configurations).
[ ] Trained Graph Neural Network surrogate with parity metric 
𝑅
2
>
0.92
R 
2
 >0.92
 on formation energy.
[ ] Bayesian Optimization trajectory identifying top-candidate doped structures with low migration barrier (
𝐸
𝑎
<
0.35
 eV
E 
a
​
 <0.35 eV
).
👨‍💻 Principal Investigator
Mahdi Oftadeh
Focus: Autonomous Materials Discovery, Computational Defect Engineering, Solid-State Battery Cathodes.
📜 License
This sub-project is maintained under the MIT License.
