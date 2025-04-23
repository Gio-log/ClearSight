# ClearSight
Work in progress
## What is ClearSight
<p align="justify">
  ClearSight is a desktop app for Windows or Linux to monitor and test network securityIt provides a comprehensive view of your network's health and security by allowing you to perform network scans, sniff traffic, monitor system stats, and log results—all from a sleek, user-friendly interface.

Built with PyQt5, ClearSight features multiple tabs to organize key functionalities:
<ul>
  <li>Scan Network: Run network discovery scans (using Nmap or other tools) to detect devices and open ports on your network.</li>
  <li>Sniff Traffic: Capture and analyze network packets to detect suspicious activity (with integration for tools like PyShark).</li>
  <li>Monitor: Monitor real-time system and network statistics such as bandwidth usage, CPU, and memory.</li>
  <li>Logs: View and store logs of network scans, traffic analysis, and system monitoring.</li>
</ul>
Features:
    Work in progress
Requirements:
<ul>
  <li>Python 3.x</li>
  <li>PyQt5</li>
  <li>Scapy / Nmap (for scanning)</li>
  <li>PyShark (for packet sniffing)</li>
  <li>Psutil (for system monitoring)</li>
</ul>
</p>

## To-Do List

<ol>
  <li>GUI Layout & Navigation</li>
  <ul>
    <li>Design basic window layout using PyQt5.</li>
    <li>Create main window with tabs(Scan Network, Sniff Traffic, Monitor, Logs).</li>
    <li>Add navigation between tabs with a clean UI.</li>
  </ul>
  
  <li>Scan Network Tab</li>
  <ul>
    <li>Implement Nmap integration for network scanning (subnet discovery, port scanning).</li>
    <li>Create a button to trigger the scan.</li>
    <li>Display scan results in a readable format (e.g., device IPs, open ports).</li>
    <li>Add error handling for failed scans.</li>
  </ul>
    
  <li>Sniff Traffic Tab</li>
  <ul>
    <li>Integrate PyShark for packet sniffing and display.</li>
    <li>Show captured packets in real-time.</li>
    <li>Filter and display different types of packets (ICMP, TCP, UDP, etc.).</li>
    <li>Option to stop the sniffing process and display results.</li>
  </ul>
  
  <li>Monitor Tab</li>
  <ul>
    <li>Use Psutil to monitor system stats (CPU, memory, network usage).</li>
    <li>Display real-time graphs or stats (e.g., bandwidth usage, CPU load).</li>
    <li>Option to track system usage history for the session.</li>
    <li>Add alerts for unusual system activity (e.g., high CPU usage).</li>
  </ul>

  <li>Logs Tab</li>
  <ul>
    <li>Implement log display for scan results and system stats.</li>
    <li>Enable saving logs to a file (e.g., .txt or .json).</li>
    <li>Allow searching and filtering logs (date, type, severity).</li>
    <li>Option to clear logs or export them.</li>
  </ul>

  <li>Advanced Features (Optional)</li>
  <ul>
    <li>Implement packet analysis for suspicious activity (e.g., DDoS).</li>
    <li>Integrate vulnerability scanners (e.g., Scanners like OpenVAS or Vulners API).</li>
    <li>Add penetration testing tools (e.g., SQLMap, Hydra for brute-force attacks).</li>
    <li>Implement a feature for scheduled scans or continuous monitoring.</li>
  </ul>

  <li>Polishing & Final Touches</li>
  <ul>
    <li>Style the app using Qt stylesheets (modern and clean design).</li>
    <li>Add tooltips and help text for UI elements.</li>
    <li>Test the app on multiple platforms (Windows, Mac, Linux).</li>
    <li>Conduct bug testing and fix issues.</li>
    <li>Write README and document the project.</li>
  </ul>

  <li>Deployment & Maintenance</li>
  <ul>
    <li>Package the app for distribution (e.g., executable for Windows/macOS/Linux).</li>
    <li>Create a user manual or guide for setup and usage.</li>
    <li>Set up continuous integration (CI) for automated testing.</li>
    <li>Regularly update with new security tools or features.</li>
  </ul>
</ol>
