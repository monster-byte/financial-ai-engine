from dataclasses import dataclass
from typing import List

from src.core.financial_context import FinancialContext


@dataclass
class MarketSequence:
    """
    Ordered sequence of financial contexts.

    The neural model will eventually use this temporal structure
    to learn how financial states evolve over time.
    """

    contexts: List[FinancialContext]

    def add(self, context: FinancialContext) -> None:
        self.contexts.append(context)

    def size(self) -> int:
        return len(self.contexts)

    def latest(self) -> FinancialContext:
        if not self.contexts:
            raise ValueError("Market sequence is empty.")

        return self.contexts[-1]

    def previous(self) -> FinancialContext:
        if len(self.contexts) < 2:
            raise ValueError(
                "At least two market contexts are required."
            )

        return self.contexts[-2]
