from dataclasses import dataclass
from typing import Dict


@dataclass
class MarketRegimeResult:
    regime: str
    probabilities: Dict[str, float]
    risk_level: str
    confidence: float
    signal_quality: float
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

    # Calculate the overall market score.
    score = (
        equity_trend * 0.25
        + breadth * 0.20
        - volatility * 0.10
        - rates * 0.10
        - usd * 0.10
        + credit * 0.15
        + growth * 0.10
    )

    # Determine the dominant market regime.
    if score >= 0.35:
        regime = "risk_on"

        probabilities = {
            "risk_on": 60 + score * 20,
            "transition": 30 - score * 10,
            "risk_off": 10,
        }

    elif score <= -0.35:
        regime = "risk_off"

        probabilities = {
            "risk_on": 10,
            "transition": 30 - abs(score) * 10,
            "risk_off": 60 + abs(score) * 20,
        }

    else:
        regime = "transition"

        probabilities = {
            "risk_on": 25 + score * 25,
            "transition": 50,
            "risk_off": 25 - score * 25,
        }

    # Normalize probabilities to 100%.
    total = sum(probabilities.values())

    probabilities = {
        key: round(value / total * 100, 2)
        for key, value in probabilities.items()
    }

    # Determine risk level.
    if regime == "risk_off":
        risk_level = "high"
    elif regime == "transition":
        risk_level = "medium"
    else:
        risk_level = "low"

    # Detect conflicting signals.
    conflicts = {}

    if equity_trend > 0 and growth < 0:
        conflicts["equity_growth"] = (
            "Bullish equities vs slowing growth"
        )

    if rates > 0 and equity_trend > 0:
        conflicts["rates_equities"] = (
            "Rising rates vs bullish equities"
        )

    if usd > 0 and equity_trend > 0:
        conflicts["usd_equities"] = (
            "Strong USD vs bullish equities"
        )

    # Calculate signal quality.
    signal_quality = 100

    # Conflicting signals reduce signal quality.
    signal_quality -= len(conflicts) * 15

    # Strong breadth improves signal quality.
    if abs(breadth) >= 0.70:
        signal_quality += 10

    # Strong credit confirmation improves signal quality.
    if abs(credit) >= 0.70:
        signal_quality += 10

    # Extreme volatility reduces signal quality.
    if abs(volatility) >= 0.70:
        signal_quality -= 15

    signal_quality = max(0, min(100, signal_quality))

    confidence = probabilities[regime]

    return MarketRegimeResult(
        regime=regime,
        probabilities=probabilities,
        risk_level=risk_level,
        confidence=round(confidence, 2),
        signal_quality=round(signal_quality, 2),
        conflicts=conflicts,
    )
