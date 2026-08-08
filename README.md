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
