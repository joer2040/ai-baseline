#!/usr/bin/env python3
"""Validate UCA configuration without modifying repository files (Python >= 3.10)."""

import json
from pathlib import Path
import sys

try:
    from jsonschema import Draft202012Validator
    from jsonschema.exceptions import SchemaError
except ImportError:
    print("ERROR: falta jsonschema. Ejecuta: python -m pip install -r requirements-dev.txt")
    raise SystemExit(1)

ROOT = Path(__file__).resolve().parents[1]
FILE_FIELDS = (
    ("context", "index"),
    ("context", "startup_protocol"),
    ("memory", "state"),
    ("workflows", "handoff_template"),
    ("workflows", "handoff_protocol"),
)
DIRECTORY_FIELDS = (("memory", "handoffs_dir"),)


def load_json(path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, ValueError) as exc:
        raise ValueError(f"{path.name}: no se pudo leer JSON UTF-8: {exc}") from exc


def validate(root):
    """Return all detectable errors; resolve paths relative to root."""
    root = root.resolve()
    errors = []
    try:
        schema = load_json(root / ".ai/settings.schema.json")
        settings = load_json(root / ".ai/settings.json")
        Draft202012Validator.check_schema(schema)
    except (ValueError, SchemaError) as exc:
        return [str(exc)]

    for error in Draft202012Validator(schema).iter_errors(settings):
        field = ".".join(str(part) for part in error.absolute_path) or "<raiz>"
        errors.append(f"settings.json [{field}]: {error.message}")
    if errors:
        return errors  # Do not use structurally invalid configuration.

    resolved = {}
    for fields, expected in ((FILE_FIELDS, "archivo"), (DIRECTORY_FIELDS, "carpeta")):
        for section, key in fields:
            value = settings[section][key]
            label = f"{section}.{key}"
            try:
                target = (root / value).resolve()
                if not target.is_relative_to(root):
                    errors.append(f"{label}: la ruta sale del repositorio: {value}")
                    continue
                correct_type = target.is_file() if expected == "archivo" else target.is_dir()
                if not correct_type:
                    errors.append(f"{label}: se esperaba {expected} existente: {value}")
                    continue
                resolved[label] = target
            except (OSError, RuntimeError) as exc:
                errors.append(f"{label}: no se pudo resolver {value}: {exc}")

    state = resolved.get("memory.state")
    if state is not None:
        try:
            data = state.read_bytes()
            text = data.decode("utf-8")
            # CRLF counts as one line; final newline does not add an empty line.
            # Empty file = 0 lines. LF, CRLF and CR are supported.
            normalized = text.replace("\r\n", "\n").replace("\r", "\n")
            lines = normalized.count("\n") + int(bool(normalized) and not normalized.endswith("\n"))
            memory = settings["memory"]
            if len(data) > memory["max_state_bytes"]:
                errors.append(
                    f"memory.state: {len(data)} bytes UTF-8; maximo {memory['max_state_bytes']}"
                )
            if lines > memory["max_state_lines"]:
                errors.append(
                    f"memory.state: {lines} lineas; maximo {memory['max_state_lines']}"
                )
        except (OSError, UnicodeError) as exc:
            errors.append(f"memory.state: no se pudo leer como UTF-8: {exc}")
    return errors


def main():
    errors = validate(ROOT)
    for error in errors:
        print(f"ERROR: {error}")
    if errors:
        print(f"UCA: validacion fallida ({len(errors)} errores).")
        return 1
    print("UCA: configuracion, rutas y limites del estado correctos.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

