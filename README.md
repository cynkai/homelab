# HomeLab

Personal Home SOC / Observability Lab.

## Stack

- Docker Desktop
- WSL2 Ubuntu
- Grafana
- Prometheus
- Loki
- Grafana Alloy
- Portainer
- Open WebUI
- Tailscale

## Current architecture

Metrics:
Windows Exporter -> Prometheus -> Grafana

Logs:
Docker Containers -> Alloy -> Loki -> Grafana

Management:
Docker -> Portainer

Remote Access:
MacBook -> Tailscale -> MSI GP73 HomeLab Server

## Goal

Build a personal Home Security Operations Center for cloud security,
system security, observability, eBPF, Sysmon, Falco, Suricata, Wazuh,
and AWS monitoring.

## Windows Host Components

### Windows Exporter

Windows Exporter runs directly on the Windows host and exposes
Windows system metrics to Prometheus.

- Port: `9182`
- Endpoint: `http://<windows-host>:9182/metrics`
- Used by: Prometheus
- Purpose:
  - CPU metrics
  - Memory metrics
  - Disk metrics
  - Network metrics
  - Windows service/system metrics

After reinstalling Windows:

1. Install Windows Exporter.
2. Make sure the Windows Exporter service is running.
3. Confirm port `9182` is listening.
4. Confirm Prometheus can reach `http://<windows-host>:9182/metrics`.
5. Import `grafana/dashboards/windows-exporter-dashboard.json` into Grafana.
