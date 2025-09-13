# Simple TCP Port Scanner 🔍

A beginner-friendly, single-file TCP port scanner written in Python. This repository contains `port_scanner.py`, a readable and well-documented script intended for learning how TCP port scanning works and for small, authorized network tests.

> ⚠️ **Important — Use responsibly.** Only scan networks and systems you own or have explicit permission to test. Unauthorized scanning may be illegal or violate acceptable-use policies.

---

## Features ✨

- Easy-to-read implementation using Python's `socket` module.
- Supports single ports, comma-separated lists, and ranges (e.g. `22,80,100-110`).
- Small default timeout for reasonably fast scans.
- Beginner-friendly: clear functions and inline docstrings for learning.

---

## Files

- `port_scanner.py` — The main script (single-file, runnable with Python 3).

---

## Requirements

- Python 3.7+ (should work with any modern Python 3.x)

---

## Usage 💡

Run from the command line or use the interactive prompts.

```bash
# Example 1: provide host and ports as command-line arguments
python3 port_scanner.py 192.168.1.10 "22,80,443"

# Example 2: provide only host (script will prompt for ports)
python3 port_scanner.py example.com

# Example 3: run with default (prompt) values
python3 port_scanner.py
```

### Ports format

You can provide ports in these formats:
- Single ports: `80`
- Comma-separated list: `22,80,443`
- Range: `1-1024`
- Combination: `22,80,100-110`

---

## Example output

```
Scanning 127.0.0.1 (3 ports)...

[+] Port 22 OPEN
[-] Port 80 closed
[+] Port 443 OPEN

Scan finished.
Open ports: 22, 443
```

---

## How it works (brief) 🧠

1. The script parses the ports string into a list of integers.
2. For each port it attempts a TCP connect using `socket.connect_ex` with a short timeout.
3. If `connect_ex` returns 0 the port is considered open.

This is a simple *connect scan* (also called TCP connect). It's reliable and easy to understand, but slower than more advanced techniques (SYN scans, asynchronous scanning, etc.).

---

## Recommended next steps / improvements 🚀

If you want to extend this project later, here are ideas:

- Add concurrency (threading, multiprocessing, or `asyncio`) for much faster scans.
- Allow port scanning by common service names (e.g., `http -> 80, 443`).
- Add banner grabbing to identify services running on open ports.
- Add an option to save results (JSON/CSV) for reporting.
- Add unit tests for parser and small integration tests.
- Add a `--safe` mode that rate-limits the scanner to avoid triggering IDS.

---

## Contributing

Contributions are welcome — open an issue or submit a pull request. Please follow these guidelines:

1. Describe the change and the rationale.
2. Keep code readable and well-commented.
3. Add tests where appropriate.


## AIM

`port_scanner.py` — created for educational purposes.


---

*Made with ❤️ for learning and ethical security practice.*

