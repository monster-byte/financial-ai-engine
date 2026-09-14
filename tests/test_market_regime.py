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
    assert result.probabilities["risk_on"] > 50
    assert result.confidence > 50


def test_market_conflicts():
    result = detect_market_regime(
        equity_trend=0.8,
        breadth=0.78,
        volatility=0.2,
        rates=0.7,
        usd=0.6,
        credit=0.5,
        growth=-0.5,
    )

    assert "equity_growth" in result.conflicts
    assert "rates_equities" in result.conflicts
    assert "usd_equities" in result.conflicts
