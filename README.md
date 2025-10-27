# CURL Analyzer

A Python-based diagnostic tool that uses CURL to test network connections and analyze common connectivity issues.

---

## ⚙️ Features

Connection Testing: Test HTTP/HTTPS connections to any URL
Proxy Support: Optional proxy configuration for testing through corporate networks
Automatic Issue Detection: Identifies common problems like:
- SSL certificate issues
- DNS resolution errors
- Connection timeouts
- Server connection failures
- HTTP error codes (404, 500, etc.)

Detailed Output: Provides both analyzed results and raw CURL output

---

## 🛠 Requirements

- Python 3.6+
- CURL installed on your system
- Required Python packages: `argparse`, `subprocess` (built-in modules)

---

## 🛠 Installation

Clone this repository:
bash
git clone https://github.com/yourusername/curl-diagnostic-tool.git
cd curl-diagnostic-tool

---

## 🧪 Usage

python curl\_diagnostic.py <URL>
python curl\_diagnostic.py <URL> --proxy http://proxyserver:port

---

## 🧪 Examples

# Test a simple website
python curl\_diagnostic.py https://google.com

# Test with proxy
python curl\_diagnostic.py https://example.com --proxy http://proxy.company.com:8080

# Test internal server
python curl\_diagnostic.py http://internal-server.local:8080
