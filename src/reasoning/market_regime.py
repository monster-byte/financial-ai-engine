from dataclasses import dataclass
from typing import Dict


@dataclass
class MarketRegimeResult:
    regime: str
    probabilities: Dict[str, float]
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

    score = (
        equity_trend * 0.25
        + breadth * 0.20
        - volatility * 0.10
        - rates * 0.10
        - usd * 0.10
        + credit * 0.15
        + growth * 0.10
    )

    # Convert the market score into three regime probabilities.
    risk_on = max(0, 50 + score * 50)
    risk_off = max(0, 50 - score * 50)
    transition = max(0, 100 - abs(score) * 100)

    total = risk_on + risk_off + transition

    probabilities = {
        "risk_on": round(risk_on / total * 100, 2),
        "transition": round(transition / total * 100, 2),
        "risk_off": round(risk_off / total * 100, 2),
    }

    regime = max(probabilities, key=probabilities.get)

    if regime == "risk_off":
        risk_level = "high"
    elif regime == "transition":
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

    confidence = probabilities[regime]

    return MarketRegimeResult(
        regime=regime,
        probabilities=probabilities,
        risk_level=risk_level,
        confidence=round(confidence, 2),
        conflicts=conflicts,
    )
