# AI Second Brain — UCA

Central context repository for collaborating with different
AI assistants through a shared, explicit, versioned foundation.

UCA is the organizational convention adopted in this repository.
Each application needs a compatible integration to use it.

## Entry Point

AI assistants must start by reading [_INDEX.md](_INDEX.md).
This file contains the base profile, collaboration rules,
and references needed to continue.

## Organization

| Path | Contents |
|---|---|
| _INDEX.md | Profile, rules, and context map. |
| CLAUDE.md | Redirect to the index for compatible clients. |
| .ai/settings.json | Shared paths and limits in UCA 1.0 format. |
| .ai/rules/ | Reserved location for specific rules. |
| .ai/skills/ | Reserved location for skills and contracts. |
| .ai/workflows/ | Work protocols and templates. |
| .ai/memory/_STATE.md | Current state shared across AI assistants. |
| .ai/memory/handoffs/ | Completed handoffs between sessions. |

## Starting a Session

Give the AI assistant access to the repository and instruct it:

> Read _INDEX.md in joer2040/ai-baseline. Follow the startup
> protocol and consult the shared state before continuing.
> If you cannot access a required file, say so.

The protocol is available here:
[Universal startup](.ai/workflows/startup_protocol.md).

Automatic loading depends on each client's configuration.
Storing files in GitHub does not configure applications.

## Closing or Transferring a Task

Use the [handoff protocol](.ai/workflows/handoff_protocol.md)
and the [handoff template](.ai/workflows/handoff_template.md).

Update the shared state within the authorized scope.
The state holds the current situation and handoffs record transitions.
If saving is not possible, deliver the handoff in the chat
and indicate that persistence is pending.

Each _STATE.md file is limited to 25,000 UTF-8 bytes
and 500 lines.

## Shared Configuration

[.ai/settings.json](.ai/settings.json) contains context and workflow
paths, along with the shared state limits.
All paths resolve from the repository root.
Conventions are documented in [_INDEX.md](_INDEX.md).

Each integration must interpret this UCA-specific format.
The JSON does not apply settings automatically.

### Configuration Validation

Validate .ai/settings.json against [.ai/settings.schema.json](.ai/settings.schema.json)
using a validator compatible with JSON Schema Draft 2020-12.
The schema checks fields, types, version, path formatting, and configured
limits. It does not check whether targets exist or the actual state
file size. Adding it does not install or activate an automatic validator.

### Local Repository Check

Requires Python 3.10 or later. From the repository root:

```sh
python -m pip install -r requirements-dev.txt
python scripts/validate_uca.py
```

The script locates the root from its own location; it does not depend
on the directory from which it is run. It only reads files and reports errors.
It validates the JSON against its schema, checks targets as files or
directories, and ensures resolved paths remain within the repository.
It also checks that memory.state is UTF-8 and stays within its limits.

Bytes are counted from the saved file, including line endings.
For line counting, LF, CRLF, and CR each count as one line break;
a final line break does not add an empty line, and an empty file has 0 lines.

Returns 0 when all checks pass and 1 on errors, including invalid JSON,
inaccessible files, or a missing dependency. Execution in
GitHub Actions remains pending.

## Private Configuration

.gitignore excludes the agreed local context and configuration files,
as well as environment variable files.

Do not store credentials or secrets in versioned files.
Local files are not loaded automatically merely because they exist.

## Pending Items

- Project organization and registration.
- Capability audit for each environment.
- Incorporation of skills, plugins, MCP servers, and connectors.
- Entry mechanism configuration for each application.
