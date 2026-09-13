from src.reasoning.market_regime import detect_market_regime


def test_bullish_market():
    result = detect_market_regime(
        equity_trend=0.8,
        breadth=0.78,
        volatility=0.2,
        rates=0.3,
        usd=0.2,
        credit=0.7,
        growth=0.2,
    )

    assert result.regime == "risk_on"
    assert result.probability > 50
    assert result.confidence > 50
