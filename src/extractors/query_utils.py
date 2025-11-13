from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional

@dataclass
class SearchQuery:
    raw: str
    built: str

def normalize_query(line: str) -> Optional[str]:
    cleaned = line.strip()
    if not cleaned or cleaned.startswith("#"):
        return None
    return cleaned

def load_queries(input_path: Path) -> List[str]:
    if not input_path.is_file():
        raise FileNotFoundError(f"Input file not found at {input_path}")
    queries: List[str] = []
    with input_path.open("r", encoding="utf-8") as f:
        for line in f:
            normalized = normalize_query(line)
            if normalized:
                queries.append(normalized)
    return queries

def build_search_query(
    raw_query: str,
    country_code: Optional[str] = None,
    exact_match: bool = True,
) -> SearchQuery:
    base = raw_query.strip()
    if not base:
        raise ValueError("raw_query must not be empty")

    if exact_match:
        term = f'"{base}"'
    else:
        term = base

    query_parts = [f"site:linkedin.com/in {term}"]
    if country_code:
        query_parts.append(f"location:{country_code}")

    built = " ".join(query_parts)
    return SearchQuery(raw=raw_query, built=built)