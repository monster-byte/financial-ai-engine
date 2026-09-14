from src.evaluation.track_record import TrackRecord
from src.evaluation.calibration import calibration_error


def test_calibration_error():

    tracker = TrackRecord()

    record_1 = tracker.add_prediction(
        market="NASDAQ-100",
        prediction="risk_on",
        probability=80.0,
        confidence=85.0,
        signal_quality=90.0,
        momentum=80.0,
    )

    record_2 = tracker.add_prediction(
        market="NASDAQ-100",
        prediction="risk_off",
        probability=60.0,
        confidence=65.0,
        signal_quality=70.0,
        momentum=40.0,
    )

    tracker.update_result(record_1, "risk_on")
    tracker.update_result(record_2, "risk_on")

    error = calibration_error(tracker)

    assert error == 50.0
