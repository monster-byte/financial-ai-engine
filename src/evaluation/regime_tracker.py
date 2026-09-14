from src.reasoning.market_regime import MarketRegimeResult
from src.evaluation.track_record import TrackRecord


def record_market_regime(
    tracker: TrackRecord,
    market: str,
    result: MarketRegimeResult,
) -> None:

    tracker.add_prediction(
        market=market,
        prediction=result.regime,
        probability=result.probabilities[result.regime],
        confidence=result.confidence,
        signal_quality=result.signal_quality,
        momentum=result.momentum,
    )
