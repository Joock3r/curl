import argparse
import subprocess

def run_curl(url, proxy=None):
    cmd = ["curl", "-v", url]
    if proxy:
        cmd += ["--proxy", proxy]

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        output = result.stderr + result.stdout
        return analyze_output(output)
    except subprocess.TimeoutExpired:
        return {"status": "error", "message": "Timeout expired"}
    except Exception as e:
        return {"status": "error", "message": str(e)}

def analyze_output(output):
    issues = []
    if "SSL certificate problem" in output:
        issues.append("SSL certificate issue")
    if "Could not resolve host" in output:
        issues.append("DNS resolution error")
    if "Connection timed out" in output:
        issues.append("Connection timeout")
    if "Failed to connect" in output:
        issues.append("Failed to connect to server")
    if "HTTP/1.1 404" in output or "HTTP/2 404" in output:
        issues.append("HTTP 404 - Page not found")
    if "HTTP/1.1 500" in output or "HTTP/2 500" in output:
        issues.append("HTTP 500 - Server error")

    return {
        "status": "success" if not issues else "error",
        "issues": issues,
        "raw_output": output
    }

def main():
    parser = argparse.ArgumentParser(description="CURL analysis tool for connection diagnostics")
    parser.add_argument("url", help="URL to test")
    parser.add_argument("--proxy", help="Proxy (e.g., http://proxyserver:port)", default=None)
    args = parser.parse_args()

    result = run_curl(args.url, args.proxy)

    print("\n--- CURL Analysis Results ---")
    print(f"Status: {result['status']}")
    if result['issues']:
        print("Detected Issues:")
        for issue in result['issues']:
            print(f"- {issue}")
    else:
        print("No issues detected.")
    print("\n--- Full CURL Output ---")
    print(result['raw_output'])

if __name__ == "__main__":
    main()