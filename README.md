# AegisAgent — Multimodal Guardian Agent

AegisAgent is a multimodal, multi-agent system for real-time personal safety, triage, and accessibility.  
This repository contains a reproducible demo, modular agent code, tools, memory services, and deployment helpers.

## Contents
- `main.py` — entrypoint for demo and local runs
- `agents/` — agent implementations (vision, reasoner, alert, accessibility)
- `tools/` — integrations (camera/microphone connector, Twilio wrapper)
- `memory/` — session & long-term memory modules
- `utils/` — logging and configuration loaders
- `kaggle_writeup.md` — submission-ready writeup
- `video_script.txt` — 3-minute video script
- `notebooks/demo_notebook.ipynb` — demo notebook (placeholder)

## Quickstart (local demo)
1. Copy `config.example.py` -> `config.py` and fill secrets.
2. Create virtual env: `python -m venv venv && source venv/bin/activate`
3. Install deps: `pip install -r requirements.txt`
4. Run demo: `python main.py --demo`

> The demo uses synthetic events (simulated fall / scream) for easy offline testing.

## Reproducibility & deployment
- Dockerfile included for containerized runs.
- `deploy/` (not included) can contain Terraform/Cloud Run scripts if you choose to deploy.
- Observability: code writes structured logs to `logs/` (console by default). Integration with Prometheus/Grafana is described in docs.

## License & Winner obligations
If this project wins, deliverables will be licensed under CC-BY-SA 4.0 per competition rules. See `kaggle_writeup.md` for details.

## Notes
- **No API keys** are included. Do not commit your `config.py` with secrets.
- This scaffold is meant to be extended — replace the lightweight perception models with optimized models for production.
