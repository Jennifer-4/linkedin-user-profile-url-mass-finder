import json
import logging
from pathlib import Path
from typing import Any, Dict, List

logger = logging.getLogger(__name__)

def export_to_json(results: List[Dict[str, Any]], output_path: Path) -> None:
    logger.info("Writing %d records to JSON file: %s", len(results), output_path)
    serializable: List[Dict[str, Any]] = []
    for item in results:
        serializable.append(
            {
                "title": str(item.get("title", "")),
                "link": str(item.get("link", "")),
                "searchQuery": str(item.get("searchQuery", "")),
            }
        )

    with output_path.open("w", encoding="utf-8") as f:
        json.dump(serializable, f, ensure_ascii=False, indent=2)