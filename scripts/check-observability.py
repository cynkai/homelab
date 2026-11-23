"""Validate Compose networking without starting any containers."""

import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def compose_config(project):
    file = ROOT / project / "compose.yaml"
    output = subprocess.check_output(
        ["docker", "compose", "-f", str(file), "config", "--format", "json"],
        text=True,
    )
    return json.loads(output)


def service_networks(config, service):
    return [
        config["networks"][key]
        for key in config["services"][service]["networks"]
    ]


if __name__ == "__main__":
    monitoring = compose_config("monitoring")
    network = monitoring["networks"]["default"]["name"]
    for service in ("prometheus", "grafana"):
        if not any(entry["name"] == network for entry in service_networks(monitoring, service)):
            raise SystemExit(f"{service} must be attached to {network}")
    for project in ("loki", "alloy"):
        config = compose_config(project)
        if not any(
            entry["name"] == network and entry.get("external")
            for entry in service_networks(config, project)
        ):
            raise SystemExit(f"{project} must join {network} as an external network")
    print(f"Prometheus, Grafana, Loki and Alloy share {network}.")
