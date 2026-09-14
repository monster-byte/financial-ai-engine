from src.evaluation.track_record import TrackRecord


def test_track_record():

    tracker = TrackRecord()

    record = tracker.add_prediction(
        market="NASDAQ-100",
        prediction="bullish",
        probability=75.0,
        confidence=80.0,
        signal_quality=85.0,
        momentum=72.0,
    )

    assert tracker.total_predictions() == 1
    assert record.market == "NASDAQ-100"
    assert record.prediction == "bullish"
    assert record.probability == 75.0

    tracker.update_result(
        record,
        actual_result="bullish",
    )

    assert record.correct is True
    assert tracker.accuracy() == 100.0
