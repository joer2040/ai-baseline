# Shared State

## Active Context
- AI Second Brain — Universal Context Architecture (UCA).
- Repository: https://github.com/joer2040/ai-baseline

## Current Objective
Define the repository's base standards and maintain continuity across AI assistants.

## Completed
- Central index with the user profile and universal rules.
- Handoff template and protocol.
- Links to both documents from _INDEX.md.
- Shared state created in .ai/memory/_STATE.md.
- .ai/memory/handoffs/ directory preserved through .gitkeep.
- References to both locations added to _INDEX.md.

- .gitignore created for private context and environment variables.
- Startup guide created in .ai/workflows/startup_protocol.md.
- Startup guide linked from _INDEX.md.
- README.md updated with the approved usage guide.
- Topic rule template created in .ai/rules/_TEMPLATE.md.
- Template linked from _INDEX.md.
- UCA 1.0 shared configuration added in .ai/settings.json.
- Configuration conventions documented in _INDEX.md and README.md.

- Schema created in .ai/settings.schema.json and documented in the index and README.
- Current configuration validated with jsonschema Draft202012Validator;
  13 invalid cases rejected during checks before publication.

- Local validator created in scripts/validate_uca.py, with
  jsonschema==4.26.0 in requirements-dev.txt and commands in README.
- Checks before publication: 33 passed;
  configuration, paths, UTF-8, limits, LF/CRLF/CR, and exit codes 0/1.
- Checks confirmed that the validator does not modify files.
- Repository documentation, templates, comments, schema descriptions,
  and validator messages translated into English at the user's request.
- Translation checks: all 33 validator checks passed again; schema rules,
  configured paths, ignore patterns, and Markdown link targets preserved.

- GitHub Actions workflow added at .github/workflows/validate_uca.yml.
- Workflow YAML and local validator checked before publication.
- First GitHub Actions execution completed successfully:
  https://github.com/joer2040/ai-baseline/actions/runs/43328243954
- Verified push-triggered run for commit 7db6c45c08a7746ff3dd6016c59eb018ed23847a.
- Dependency installation and the Validate repository step both succeeded.

## Approved Decisions
- JSON Schema Draft 2020-12 approved for UCA 1.0 configuration.
- UCA 1.0 configuration: paths relative to the root and approved limits.
- Local settings cannot change shared rules, authorizations, or limits.
- Approved topic rule format: Markdown with XML tags.
- The rule template is not an active rule.
- Shared state: .ai/memory/_STATE.md.
- Completed handoffs: .ai/memory/handoffs/.
- State limited to 25,000 UTF-8 bytes and 500 lines.
- State and handoffs shared across AI assistants.
- Project organization postponed by the user.
- Audit and inventory postponed by the user.
- Universal startup guide approved; each client needs
  a compatible mechanism to load the index.
- Repository content translated into English; the user's default
  collaboration language remains Spanish.

- Automated checks approved for pull requests, pushes to main,
  and manual dispatches, with read-only repository permissions.

## Pending Items
- Define the remaining modules with the user.
- Keep projects and the audit pending until further instruction.

## Next Step
- Agree on the next repository standards module with the user.
- The GitHub Actions module is implemented and its first push run verified.
- Pull request and manual triggers are configured but were not exercised
  during this task.
- The user authorized publication and first-run verification.
- Audit, inventories, and project organization remain postponed.
