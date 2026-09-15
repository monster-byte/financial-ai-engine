from dataclasses import dataclass, field
from typing import List

from src.core.market_state import MarketState
from src.core.cross_asset import CrossAssetRelationships
from src.core.financial_event import FinancialEvent


@dataclass
class FinancialContext:
    """
    Unified financial context presented to the future neural model.
    """

    market_state: MarketState
    relationships: CrossAssetRelationships
    events: List[FinancialEvent] = field(default_factory=list)

    def event_impact(self) -> float:
        """
        Aggregate the impact of available financial events.
        """

        if not self.events:
            return 0.0

        total = sum(
            event.impact_score()
            for event in self.events
        )

        return round(total / len(self.events), 4)

    def market_vector(self) -> list[float]:
        """
        Return the numerical representation of the current
        financial environment.
        """

        return self.market_state.to_vector()

    def relationship_vector(self) -> list[float]:
        """
        Return the cross-asset relationship strengths.
        """

        return list(
            self.relationships.all_relationships().values()
        )
