"""Tests for the engagement-based pre-filter that bounds AI call volume."""

from datetime import datetime, timezone

from src.models import ContentItem, SourceType
from src.orchestrator import HorizonOrchestrator


def _item(
    title: str,
    source_type: SourceType,
    meta: dict | None = None,
    url: str = "https://example.com/story",
) -> ContentItem:
    return ContentItem(
        id=f"{source_type.value}:test:{title}",
        source_type=source_type,
        title=title,
        url=url,
        published_at=datetime.now(timezone.utc),
        metadata=meta or {},
    )


def _orchestrator() -> HorizonOrchestrator:
    """Construct an orchestrator without running __init__ (pure method tests)."""
    return HorizonOrchestrator.__new__(HorizonOrchestrator)


def test_prefilter_truncates_to_max_analyze():
    items = [
        _item(f"item{i}", SourceType.HACKERNEWS, {"score": 100})
        for i in range(60)
    ]
    kept, skipped = _orchestrator()._prefilter_for_analysis(items, 45)
    assert len(kept) == 45
    assert skipped == 15


def test_prefilter_keeps_at_least_one_per_source_type():
    items = (
        [_item(f"hn{i}", SourceType.HACKERNEWS, {"score": 1}) for i in range(20)]
        + [_item(f"rss{i}", SourceType.RSS, {}) for i in range(10)]
        + [_item(f"tg{i}", SourceType.TELEGRAM, {}) for i in range(5)]
    )
    kept, skipped = _orchestrator()._prefilter_for_analysis(items, 20)
    types = {item.source_type.value for item in kept}
    assert {"hackernews", "rss", "telegram"} <= types
    assert len(kept) == 20
    assert skipped == 15


def test_prefilter_prefers_high_engagement():
    items = [
        _item("low", SourceType.HACKERNEWS, {"score": 5}),
        _item("high", SourceType.HACKERNEWS, {"score": 500}),
        _item("med", SourceType.HACKERNEWS, {"score": 100}),
    ]
    kept, _ = _orchestrator()._prefilter_for_analysis(items, 2)
    titles = {item.title for item in kept}
    assert "high" in titles and "med" in titles and "low" not in titles


def test_heuristic_priority_aggregates_signals():
    orch = _orchestrator()
    strong = _item(
        "strong", SourceType.HACKERNEWS, {"score": 3000, "descendants": 3000}
    )
    weak = _item("weak", SourceType.REDDIT, {"views": 20000})
    assert orch._heuristic_priority(strong) > orch._heuristic_priority(weak)
