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

## Start and check telemetry

Run these commands from the repository root with Docker Desktop running.

```sh
python3 scripts/check-observability.py
docker compose -f monitoring/compose.yaml up -d
docker compose -f loki/compose.yaml up -d
docker compose -f alloy/compose.yaml up -d
```

The monitoring project creates the shared `monitoring_default` network.
Start it first so Loki and Alloy can join that network. Grafana reads
Prometheus at `http://prometheus:9090` and Loki at `http://loki:3100`.
Alloy sends logs to Loki on the same network.

Open Grafana at <http://localhost:3001>. In Explore, run `up` against
Prometheus and `{container=~".+"}` against Loki. If Loki returns no logs,
check its readiness at <http://localhost:3100/ready> and inspect Alloy
with `docker compose -f alloy/compose.yaml logs --tail=30 alloy`.

When stopping the stack, take Alloy and Loki down before the monitoring
project. Docker can remove the shared network once those containers are gone.

## Goal

Build a personal Home Security Operations Center for cloud security,
system security, observability, eBPF, Sysmon, Falco, Suricata, Wazuh,
and AWS monitoring.

## Next step

Once this lab server is up, work continues in
[todo-cli](https://github.com/cynkai/todo-cli), which builds on top of it.

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
