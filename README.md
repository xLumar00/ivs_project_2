# IVS Calculator

> A cross-platform graphical calculator, mathematical library, and statistical profiling utility developed as a collaborative software engineering team project (IVS) at Brno University of Technology (FIT VUT).

![Calculator Screenshot](screenshot.png)

---

## 1. Overview & Context

This project was developed for the **Software Engineering (IVS)** course at Brno University of Technology (FIT VUT) in Spring 2026. The objective was to design, implement, test, profile, document, package, and deploy a multi-functional graphical desktop calculator adhering to professional software engineering standards.

As **Team Lead and Infrastructure Engineer** for team *Absolute Zeros*, my responsibilities focused on project infrastructure, authoring the developer `Makefile`, implementing Linux system deployment scripts (`install.sh`, `uninstall.sh`), managing milestone deliveries, and resolving system packaging challenges.

Key technologies utilized:
- **Programming Language:** Python 3 (Tkinter, CustomTkinter)
- **Build & Lifecycle Automation:** GNU Make, Bash
- **Documentation:** Doxygen, Markdown, PDF
- **Target Environments:** Ubuntu 24.04 (Primary verification platform), Fedora Linux, macOS, Windows

---

## 2. Architecture & Design

- **Core Components:**
  - **GUI Presentation Layer (`src/ui.py`):** Dark-mode interface built on `customtkinter` with arithmetic, scientific, and memory functions.
  - **Mathematical Engine (`src/math_lib.py`):** Decoupled, pure mathematical backend implementing fundamental arithmetic, factorials, powers, and roots.
  - **Profiling Tool (`src/stddev.py`):** Standalone CLI utility for computing sample standard deviation on large numerical datasets.
  - **Automated Test Suite (`src/test_math_lib.py`, `src/tests_stddev.py`):** Unit testing suite validating calculation accuracy, mathematical edge cases, and error conditions.
  - **Deployment Automation (`install/install.sh`, `src/Makefile`):** System installer, uninstaller, wrapper generation, and packaging targets.
- **IPC / Protocols / Data Flow:**
  - GUI inputs are sanitized and dispatched directly to the stateless `math_lib` core.
  - Profiling utility consumes numbers streamed via `stdin` or loaded from disk and outputs computed statistical metrics to `stdout`.
- **Constraints / Design Decisions:**
  - Chose `customtkinter` over heavier frameworks (e.g. PyQt) to reduce packaging footprint and simplify dependency resolution in Linux testing environments.
  - Enforced POSIX-standard file placement (`/opt/ivs_calc`, `/usr/local/bin`, `/usr/share/applications/`).

```
[User Input / GUI (ui.py)]  ──►  [Math Core (math_lib.py)]  ──►  Result Display
           ▲
           │
[System Wrappers: /usr/local/bin]  ◄──  [Installer (install.sh)]  ◄──  [Makefile]
```

---

## 3. Directory Structure

```text
.
├── assets/             # Graphical assets and application icons
├── doc/                # Doxygen configuration and generated documentation
├── install/            # System deployment automation
│   ├── install.sh      # Bash installer (system integration, /opt deployment)
│   └── uninstall.sh    # Idempotent cleanup script
├── mockup/             # UI/UX design mockups
├── plan/               # Project schedule, milestones, and planning documents
├── profiling/          # Statistical profiling datasets and performance reports
├── src/                # Primary source code
│   ├── Doxyfile        # Doxygen configuration
│   ├── main.py         # Application entry point
│   ├── Makefile        # Project build and orchestration automation
│   ├── math_lib.py     # Standalone mathematical engine
│   ├── stddev.py       # Standard deviation profiling CLI tool
│   ├── test_math_lib.py# Unit test suite for mathematical operations
│   └── ui.py           # CustomTkinter GUI implementation
├── debugging.png       # Profiling and debugging screenshot
├── LICENSE             # GNU GPL v3 license terms
├── manual.pdf          # User manual and operation guide
├── README.md           # Documentation
├── requirements.txt    # Python package dependencies
└── screenshot.png      # Application GUI screenshot
```

---

## 4. Technical Deep-Dive / Key Features

### Developer Automation (`src/Makefile`)
- **Path:** `src/Makefile`
- **Domain & Tech:** Build engineering, GNU Make, Python packaging
- **Implementation Details:** Unifies the developer experience across milestones with clean targets:
  - `make all`: Installs dependencies via `pip` with modern distribution compatibility flags.
  - `make run`: Boots the calculator interface.
  - `make test`: Runs unit tests validating numerical operations.
  - `make doc`: Compiles Doxygen technical reference documentation into `doc/`.
  - `make pack`: Automates clean delivery bundling, stripping redundant files and validating archive structures.
  - `make install` / `make uninstall`: Delegates to root system deployment scripts.

### Linux System Deployment & Uninstaller (`install/install.sh`, `install/uninstall.sh`)
- **Path:** `install/install.sh`, `install/uninstall.sh`
- **Domain & Tech:** Systems administration, Bash scripting, FreeDesktop standards
- **Implementation Details:**
  - Enforces effective root user verification (`$EUID -ne 0`).
  - Verifies and prompts for prerequisite runtimes (`python3`, `pip3`, `python3-tk`).
  - Installs application source files into `/opt/ivs_calc`.
  - Creates executable wrappers in `/usr/local/bin/Calculator_IVS` and `/usr/local/bin/stddev` for direct invocation from system `$PATH`.
  - Installs FreeDesktop `.desktop` entry at `/usr/share/applications/ivs-calculator.desktop` with application icons.
  - Accompanied by `uninstall.sh` ensuring clean, idempotent removal of all installed files, wrappers, and desktop entries.

### Python Packaging Hurdles & PEP 668 Mitigation
- **Path:** `src/Makefile`, `install/install.sh`
- **Domain & Tech:** Python packaging, modern Linux distributions (Ubuntu 24.04 / Fedora)
- **Implementation Details:** Handled modern Linux distribution restrictions imposed by **PEP 668** ("externally managed environment"), which block `pip install` without virtual environments. Configured reproducible build and installation routines via safe user and package bypass flags (`--break-system-packages`).

---

## 5. Prerequisites & Environment

- **OS / Platform:** Ubuntu 24.04 LTS (Primary target), Fedora Linux, Arch, Windows, macOS
- **Compilers / Runtimes:** Python 3.10+, GNU Make
- **System Dependencies / Daemons:** `python3-tk` (Tkinter bindings), `python3-pip`, Doxygen (for documentation generation)

---

## 6. Build & Installation

```bash
# Clone the repository
git clone git@github.com:xLumar00/ivs_project_2.git
cd ivs_project_2/src

# Install project dependencies
make all

# Optional: Install system-wide to /opt/ivs_calc and /usr/local/bin
sudo make install
```

---

## 7. Usage & Examples

```bash
# Launch the graphical calculator locally
cd src
make run

# If installed system-wide, launch directly from any terminal
Calculator_IVS

# Execute unit test suites
make test

# Generate technical Doxygen documentation
make doc

# Uninstall system-wide deployment
sudo make uninstall
```

---

## 8. Engineering Post-Mortem & Known Issues

- **Distribution Packaging Trade-Offs:** The installation script directly installs Python dependencies into system packages using `apt` and `--break-system-packages`. While functional in clean testing containers, an isolated virtual environment (`/opt/ivs_calc/venv`) is the preferred enterprise Linux practice to completely prevent system Python contamination.
- **Relative Path Script Dependencies:** The `install.sh` script originally assumed execution from the `install/` directory via relative paths (`../src`). Dynamic path discovery via `$(dirname "$0")` provides more resilient location-independent invocation.
- **Agile Milestone Variance:** Milestone planning experienced an initial 1–2 week schedule shift due to underestimating the complexity of GUI integration and packaging restrictions. Reallocating team priorities during the integration phase allowed the team to deliver all core requirements and achieve a 100% evaluation score across all members.

---

## 9. Roadmap & Future Improvements

- [ ] Modernize the installer to provision a dedicated virtual environment under `/opt/ivs_calc/venv`.
- [ ] Add distro-agnostic dependency resolution (adding `dnf` and `pacman` detection alongside `apt`).
- [ ] Implement automated CI/CD pipeline using GitHub Actions to run unit tests and linters across multiple Python versions.

---

## 10. Notes / Attribution

- **Authors:** Team *Absolute Zeros* (FIT VUT)
  - Marek Lupták (`xluptam00`) – Team Lead, Infrastructure, Makefile, Installer, Uninstaller, Integration
  - Timotej Lukotka (`xlukott00`) – Mathematical Engine, Unit Tests
  - Matúš Heldi (`xheldim00`) – Graphical User Interface (GUI)
  - Timotej Vojta (`xvojtat00`) – Profiling & Standard Deviation
- **License:** GNU General Public License v3.0 (see `LICENSE`)
