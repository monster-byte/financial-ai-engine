from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class FinancialEvent:
    """
    Representation of an event that can influence financial markets.
    """

    timestamp: datetime
    event_type: str
    source: str
    title: str

    # Expected market impact
    impact: float

    # Confidence in the estimated impact
    confidence: float

    # Optional affected asset or market
    affected_asset: Optional[str] = None

    # Optional textual context
    context: Optional[str] = None

    def impact_score(self) -> float:
        """
        Combine impact magnitude with confidence.
        """

        return round(
            self.impact * self.confidence,
            4,
        )
