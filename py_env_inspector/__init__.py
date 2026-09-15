import os
import re
from typing import Dict, List, Set, Optional
from dataclasses import dataclass

@dataclass
class AuditReport:
    required_keys: Set[str]
    missing_keys: Set[str]
    empty_keys: Set[str]

    @property
    def is_valid(self) -> bool:
        return len(self.missing_keys) == 0 and len(self.empty_keys) == 0

def parse_env_file(file_content: str) -> Set[str]:
    """Extract environment variable names from .env or .env.example content."""
    keys = set()
    for line in file_content.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        match = re.match(r"^([a-zA-Z_][a-zA-Z0-9_]*)\s*=", line)
        if match:
            keys.add(match.group(1))
    return keys

def audit_env(
    example_content: Optional[str] = None,
    example_path: Optional[str] = None,
    target_env: Optional[Dict[str, str]] = None,
) -> AuditReport:
    """Audit target environment against .env.example template."""
    if example_content is None and example_path is not None:
        with open(example_path, "r", encoding="utf-8") as f:
            example_content = f.read()

    example_content = example_content or ""
    required_keys = parse_env_file(example_content)
    env = os.environ if target_env is None else target_env

    missing = set()
    empty = set()

    for key in required_keys:
        if key not in env:
            missing.add(key)
        elif not str(env[key]).strip():
            empty.add(key)

    return AuditReport(required_keys=required_keys, missing_keys=missing, empty_keys=empty)
