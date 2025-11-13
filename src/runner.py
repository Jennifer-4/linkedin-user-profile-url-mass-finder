import json
import logging
import os
from pathlib import Path
from typing import Any, Dict, List

from extractors.query_utils import load_queries, build_search_query, SearchQuery
from extractors.profile_searcher import LinkedInProfileSearcher
from outputs.exporters import export_to_json

def load_settings(config_path: Path) -> Dict[str, Any]:
    if not config_path.is_file():
        raise FileNotFoundError(f"Settings file not found at {config_path}")
    with config_path.open("r", encoding="utf-8") as f:
        data = json.load(f)
    return data

def resolve_project_paths(settings: Dict[str, Any]) -> Dict[str, Any]:
    root_dir = Path(__file__).resolve().parents[1]
    resolved = settings.copy()
    input_file = settings.get("input_file", "data/inputs.sample.txt")
    output_file = settings.get("output_file", "data/sample_output.json")

    resolved["input_file"] = (root_dir / input_file).resolve()
    resolved["output_file"] = (root_dir / output_file).resolve()
    resolved["root_dir"] = root_dir
    return resolved

def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s - %(message)s",
    )
    logger = logging.getLogger("runner")

    env_config = os.getenv("LUF_SETTINGS_FILE")
    if env_config:
        config_path = Path(env_config).expanduser().resolve()
    else:
        config_path = Path(__file__).resolve().parent / "config" / "settings.example.json"

    try:
        settings = load_settings(config_path)
    except Exception as e:
        logger.error("Failed to load settings file: %s", e)
        raise SystemExit(1)

    settings = resolve_project_paths(settings)

    input_path: Path = settings["input_file"]
    output_path: Path = settings["output_file"]

    logger.info("Using input file: %s", input_path)
    logger.info("Using output file: %s", output_path)

    queries_raw = load_queries(input_path)
    if not queries_raw:
        logger.warning("No valid queries found in %s", input_path)
        raise SystemExit(0)

    logger.info("Loaded %d queries", len(queries_raw))

    search_queries: List[SearchQuery] = [
        build_search_query(
            raw_query=q,
            country_code=settings.get("country_code"),
            exact_match=bool(settings.get("exact_match", True)),
        )
        for q in queries_raw
    ]

    searcher = LinkedInProfileSearcher(
        user_agent=settings.get("user_agent")
        or "LinkedInProfileFinderBot/1.0 (+https://bitbash.dev)",
        timeout=int(settings.get("request_timeout", 10)),
        max_results=int(settings.get("max_results", 5)),
    )

    all_results: List[Dict[str, Any]] = []
    for sq in search_queries:
        logger.info("Searching for query: %s", sq.raw)
        try:
            results = searcher.search(
                sq, search_engine=str(settings.get("search_engine", "duckduckgo"))
            )
            logger.info("Found %d results for '%s'", len(results), sq.raw)
            all_results.extend(results)
        except Exception as e:
            logger.exception("Search failed for '%s': %s", sq.raw, e)

    if not all_results:
        logger.warning("No results found for any query.")
    else:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        export_to_json(all_results, output_path)
        logger.info("Exported %d results to %s", len(all_results), output_path)

if __name__ == "__main__":
    main()