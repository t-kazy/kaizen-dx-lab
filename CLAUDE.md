# CLAUDE.md

This file provides guidance to Claude Code when working with this repository.

## Project Overview

kaizen-dx-lab is a multi-agent research team powered by Claude Agent SDK (Python).

## Repository Structure

```
.
├── CLAUDE.md
├── README.md
├── pyproject.toml
└── research_team/
    ├── __init__.py
    └── main.py          # Orchestrator + subagent definitions
```

## Development

- **Language**: Python 3.10+
- **Dependencies**: `claude-agent-sdk`, `anyio`
- **Install**: `pip install -e .`
- **Run**: `python -m research_team.main "Your research topic here"`
