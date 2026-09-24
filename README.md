# PyScan - Multi-Threaded TCP Port Scanner & Banner Grabber

A lightweight, concurrent TCP reconnaissance tool built purely with Python's standard library. Designed for fast port discovery and service banner extraction.

## Features
- **Zero Third-Party Dependencies:** Uses only Python built-in modules (`socket`, `concurrent.futures`, `argparse`, `random`).
- **Concurrent Scanning:** Multi-threaded socket operations using `ThreadPoolExecutor`.
- **Banner Grabbing:** Automatic service interrogation (SSH identification, HTTP probes).
- **Stealth Randomization:** Randomizes scanning sequence (`-r`) to avoid basic sequential detection.
- **Flexible Port Ranges:** Supports single ports (`-p 80`) or comprehensive ranges (`-p 1-1024`).

## Installation
Clone the repository and run directly:
```bash
git clone [https://github.com/KULLANICI_ADIN/pyscan.git](https://github.com/KULLANICI_ADIN/pyscan.git)
cd pyscan
python scanner.py -h