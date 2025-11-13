import logging
from typing import Any, Dict, List
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup

from .query_utils import SearchQuery

logger = logging.getLogger(__name__)

class LinkedInProfileSearcher:
    def __init__(self, user_agent: str, timeout: int = 10, max_results: int = 5) -> None:
        self.user_agent = user_agent
        self.timeout = timeout
        self.max_results = max_results

    def search(self, search_query: SearchQuery, search_engine: str = "duckduckgo") -> List[Dict[str, Any]]:
        search_engine = (search_engine or "duckduckgo").lower()
        if search_engine not in {"duckduckgo"}:
            logger.warning("Unsupported search engine '%s', falling back to DuckDuckGo", search_engine)
            search_engine = "duckduckgo"

        if search_engine == "duckduckgo":
            return self._search_duckduckgo(search_query)
        return []

    def _search_duckduckgo(self, search_query: SearchQuery) -> List[Dict[str, Any]]:
        query = search_query.built
        params = {"q": query}
        url = "https://duckduckgo.com/html/"

        headers = {
            "User-Agent": self.user_agent,
            "Accept-Language": "en-US,en;q=0.9",
        }

        logger.debug("Issuing DuckDuckGo request for query: %s", query)
        try:
            response = requests.get(url, params=params, headers=headers, timeout=self.timeout)
            response.raise_for_status()
        except requests.RequestException as exc:
            logger.error("DuckDuckGo request failed for '%s': %s", search_query.raw, exc)
            return []

        soup = BeautifulSoup(response.text, "html.parser")
        results: List[Dict[str, Any]] = []

        for result in soup.select("a.result__a"):
            href = result.get("href")
            title = result.get_text(strip=True)
            if not href:
                continue

            if "linkedin.com" not in href:
                continue

            parsed = urlparse(href)
            if not parsed.scheme:
                href = "https://" + href.lstrip("/")

            record = {
                "title": title,
                "link": href,
                "searchQuery": search_query.raw,
            }
            results.append(record)

            if len(results) >= self.max_results:
                break

        logger.debug("Parsed %d LinkedIn results for '%s'", len(results), search_query.raw)
        return results