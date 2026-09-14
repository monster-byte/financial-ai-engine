from src.reasoning.market_regime import detect_market_regime
from src.evaluation.track_record import TrackRecord
from src.evaluation.regime_tracker import record_market_regime


def test_record_market_regime():

    tracker = TrackRecord()

    result = detect_market_regime(
        equity_trend=0.8,
        breadth=0.78,
        volatility=0.2,
        rates=0.3,
        usd=0.2,
        credit=0.7,
        growth=0.2,
    )

    record_market_regime(
        tracker,
        market="NASDAQ-100",
        result=result,
    )

    assert tracker.total_predictions() == 1
    assert tracker.records[0].market == "NASDAQ-100"
    assert tracker.records[0].prediction == result.regime
    assert tracker.records[0].confidence == result.confidence
