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
git clone https://github.com/abdullahcevikk/pyscan.git
https://github.com/abdullahcevikk/pyscan.git
cd pyscan
python scanner.py -h
```
## Usage Examples
```bash
# Basic scan (Default: 1-1024 ports, 50 workers)
python scanner.py -t scanme.nmap.org

# Targeted range with customized thread count
python scanner.py -t scanme.nmap.org -p 20-100 -w 100

# Randomized stealth order
python scanner.py -t scanme.nmap.org -p 1-500 -r
```
## Disclaimer
This project is developed for educational purposes and authorized penetration testing only. Do not scan targets without prior mutual consent.
