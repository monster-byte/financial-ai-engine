from dataclasses import dataclass
from typing import Dict


@dataclass
class MarketRegimeResult:
    regime: str
    probability: float
    risk_level: str
    confidence: float
    conflicts: Dict[str, str]


def detect_market_regime(
    equity_trend: float,
    breadth: float,
    volatility: float,
    rates: float,
    usd: float,
    credit: float,
    growth: float,
) -> MarketRegimeResult:
    """
    Initial rule-based market regime engine.

    Inputs are normalized between -1 and +1.

    Positive values = bullish/risk-on
    Negative values = bearish/risk-off
    """

    score = (
        equity_trend * 0.25
        + breadth * 0.20
        - volatility * 0.10
        - rates * 0.10
        + usd * -0.10
        + credit * 0.15
        + growth * 0.10
    )

    if score >= 0.35:
        regime = "risk_on"
    elif score <= -0.35:
        regime = "risk_off"
    else:
        regime = "transition"

    probability = min(max(50 + score * 50, 0), 100)

    if score < -0.25:
        risk_level = "high"
    elif score < 0.15:
        risk_level = "medium"
    else:
        risk_level = "low"

    conflicts = {}

    if equity_trend > 0 and growth < 0:
        conflicts["equity_growth"] = "Bullish equities vs slowing growth"

    if rates > 0 and equity_trend > 0:
        conflicts["rates_equities"] = "Rising rates vs bullish equities"

    if usd > 0 and equity_trend > 0:
        conflicts["usd_equities"] = "Strong USD vs bullish equities"

    confidence = min(
        100,
        50 + abs(score) * 50
    )

    return MarketRegimeResult(
        regime=regime,
        probability=round(probability, 2),
        risk_level=risk_level,
        confidence=round(confidence, 2),
        conflicts=conflicts,
    )
