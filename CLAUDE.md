# CLAUDE.md

This file provides guidance to Claude Code when working with this repository.

## Project Overview

kaizen-dx-lab is a new project repository. The tech stack and structure are not yet established.

## Repository Structure

```
.
├── .claude/
│   └── settings.json
├── README.md
└── CLAUDE.md
```

## Development

No build, test, or lint tooling is configured yet. Update this section as tooling is added.

## Agent Teams

This repository has Claude Code Agent Teams enabled via `.claude/settings.json`.

### How to use

Agent Teams allow multiple Claude Code instances to work in parallel as a coordinated team. To start a team, ask Claude to create one with a description of the task and team structure.

Example:

```
Create an agent team with 3 teammates to work on this task in parallel:
- One teammate for frontend implementation
- One teammate for backend implementation
- One teammate for writing tests
```

### Guidelines for team members

- **File ownership**: Each team member should work on separate files to avoid conflicts. Do not edit the same file as another team member.
- **Task size**: Break work into self-contained units with clear deliverables (a function, a test file, a module).
- **Communication**: Use messages to share findings with other team members. Report blockers to the leader.
- **Plan approval**: For complex changes, the leader may require plan approval before implementation begins.

### Configuration

- `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS`: Enabled (`1`) in `.claude/settings.json`
- `teammateMode`: Set to `auto` (uses split panes in tmux, otherwise in-process)
