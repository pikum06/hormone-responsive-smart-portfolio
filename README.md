# Hormone-Responsive Smart Portfolio UI & Analytics

---

**ABOUT**

An interactive visual analytics dashboard and automated evaluation suite for bio-signal-driven portfolio risk management. This repository processes backtest execution logs, market indicators, and physiological stress metrics (e.g., cortisol/HRV proxies) to quantify how automated bio-circuit breakers mitigate drawdowns, control exposure decay, and preserve slippage-adjusted yield during volatile trading regimes.

---

## Repository Directory Structure

```text
.
├── data/                             # Telemetry datasets & backtest execution logs
│   ├── final_backtest_results.csv    # Simulated strategy metrics & drawdown benchmark data
│   ├── hormone_transaction_logs.csv  # On-chain smart contract leverage scaling logs
│   ├── processed_bio_signals.csv     # Extracted RMSSD & physiological stress time-series
│   └── processed_market_signals.csv  # Volatility indices & market regime telemetry
├── outcomes/                         # Performance visualizer output graphs & analytical plots
│   ├── correlation_heatmap.png       # Stress vs. market volatility correlation matrix
│   ├── Cortisol.png                  # Biomarker level tracking across market shock regimes
│   ├── final_analysis.png            # Comparative yield & capital preservation summary
│   ├── graph_1_avoided_loss.png      # Circuit breaker execution & avoided loss scatter plot
│   ├── graph_2_experience_decay.png  # Dynamic risk tolerance decay across market trauma
│   ├── graph_3_slippage_yield.png    # Cumulative yield vs. algorithmic slippage penalty
│   ├── graph_a_cortisol_beta.png     # Physiological calm vs. portfolio beta regression
│   ├── mitigation_loss.png           # Cumulative drawdown mitigation curve
│   ├── panic_active.png              # Real-time deleveraging during active panic regimes
│   └── panic_nominal.png             # Unmitigated portfolio drawdown baseline
├── research/                         # Quantitative models, signal engines & dashboard UI
│   ├── analyzer.py                   # Macroeconomic trauma & yield curve stress analyzer
│   ├── backtest_engine.py            # Local backtest simulator for bio-signal leverage adjustments
│   ├── bio_processor.py              # Biometric signal processing & RMSSD score extraction
│   ├── correlation.py                # Physiological stress vs. market volatility correlation
│   ├── cortisol_beta.py              # Cortisol-beta correlation & sustainable leverage model
│   ├── dashboard.py                  # Streamlit interactive bio-trading interface
│   ├── graph_1.py                    # Avoided loss scatter plot generator
│   ├── graph_2.py                    # Experience decay plot generator
│   ├── graph_3.py                    # Slippage & cumulative yield plot generator
│   ├── hormone.py                    # Biological circuit breaker core & leverage scaling logic
│   ├── loss_mitigation.py            # Drawdown protection & loss mitigation analyzer
│   ├── market_analyzer.py            # High-frequency market volatility & crash regime detection
│   ├── on_chain_sync.py              # Solana test validator transaction execution & state sync
│   └── rolling_prediction.py         # 30-day rolling stress level & trajectory prediction
├── .gitignore                        # Git exclusion rules
├── README.md                         # Protocol documentation & architectural overview
└── requirements.txt                  # Python dependency specifications 
```

---

## 📊 Datasets & Telemetry Benchmarks

The protocol integrates dual-stream telemetry—combining physiological stress metrics with institutional-grade macroeconomic and market volatility signals—to evaluate biological circuit breaker triggers and dynamic deleveraging:

### 1. Biometric Telemetry: SWELL Heart Rate Variability (HRV) Dataset

* **Dataset**: [SWELL Heart Rate Variability (HRV) Dataset (Kaggle)](https://www.kaggle.com/datasets/qiriro/swell-heart-rate-variability-hrv)
* **Origin**: Multimodal research conducted by Radboud University (Institute for Computing and Information Sciences) across knowledge work scenarios.
* **Experimental Stress Regimes**: Neutral working state, time pressure constraints, and unexpected email interruption spikes.
* **Physiological Indicators**: ECG-derived HRV metrics (RMSSD, SDNN, LF/HF ratios) and self-reported mental workload metrics.
* **Protocol Integration**: Ingested by `research/bio_processor.py` and `research/cortisol_beta.py` to establish `data/processed_bio_signals.csv`, deriving real-time RMSSD stress scores and cortisol-beta regressions.


### 2. Macroeconomic & Market Regimes: Algorithmic Trading Macro Stress Dataset

* **Dataset**: [Algorithmic Trading: Macro Stress & Asset Regimes (Kaggle)](https://www.kaggle.com/datasets/kanchana1990/algorithmic-trading-macro-stress-and-asset-regimes)
* **Author / Citation**: Kanchana Karunarathna
* **DOI**: [`10.34740/kaggle/dsv/14952616`](https://doi.org/10.34740/kaggle/dsv/14952616)
* **Sources**: Federal Reserve Bank of St. Louis (FRED) API and Yahoo Finance (`yfinance`).
* **Time Horizon & Scope**: Over 4,100 aligned daily trading records across global asset classes (Equities, Bonds, Crypto, Commodities) and US macro indicators.
* **Key Telemetry Features**:
  * *Market Volatility & Asset Prices*: Bitcoin (`BTC_USD`), S&P 500 (`SPY`), Nasdaq (`QQQ`), Gold (`GLD`), CBOE VIX, and 30-day rolling volatility metrics (`BTC_Rolling_Vol_30d`, `SPY_Rolling_Vol_30d`).
  * *Macro Liquidity & Credit Stress*: St. Louis Fed Financial Stress Index (`Financial_Stress_Index`), 10Y-2Y US Treasury Yield Curve Spread (`Yield_Curve_Spread`), and ICE BofA High Yield Option-Adjusted Spread (`High_Yield_Spread`).
* **Protocol Integration**: Ingested by `research/market_analyzer.py` and `research/analyzer.py` to build `data/processed_market_signals.csv`, detecting high-volatility market regimes and cross-asset panic thresholds to initiate dynamic leverage scaling in `research/hormone.py`.

---

## Analytics & System Architecture

The UI and visualization pipeline consumes processed market signals and physiological telemetry to evaluate leverage adjustments, circuit breaker triggers, and net portfolio performance.

```mermaid
graph TD
    subgraph Ingestion ["1. Telemetry Ingestion & Signal Processing"]
        A1[Biometric Telemetry / HR / RMSSD] -->|Signal Extraction| P1[research/bio_processor.py]
        A2[Market Telemetry / Volatility] -->|Regime Detection| P2[research/market_analyzer.py]
        P1 --> D1[(data/processed_bio_signals.csv)]
        P2 --> D2[(data/processed_market_signals.csv)]
    end

    subgraph Quantitative ["2. Stress Analytics & Regression Engine"]
        D1 & D2 --> C1[research/correlation.py]
        D1 & D2 --> C2[research/cortisol_beta.py]
        D1 & D2 --> C3[research/analyzer.py]
        D1 --> C4[research/rolling_prediction.py]
    end

    subgraph CircuitBreaker ["3. Biological Circuit Breaker & Deleveraging Core"]
        C1 & C2 & C3 & C4 --> H1[research/hormone.py]
        H1 -->|Dynamic Leverage Scaling| L1[research/loss_mitigation.py]
        H1 -->|Strategy Simulation| B1[research/backtest_engine.py]
        B1 --> D3[(data/final_backtest_results.csv)]
        H1 -->|Deleveraging Instructions| O1[research/on_chain_sync.py]
        O1 -->|Solana Validator Transactions| S1[Solana On-Chain Protocol]
        S1 --> D4[(data/hormone_transaction_logs.csv)]
    end

    subgraph Presentation ["4. Outcomes Visualizer & Streamlit Interface"]
        B1 --> G1[research/graph_1.py]
        B1 --> G2[research/graph_2.py]
        B1 --> G3[research/graph_3.py]
        G1 & G2 & G3 --> OUT[outcomes/*.png Artifacts]
        
        H1 & B1 & D4 --> DB[research/dashboard.py]
        DB --> UI[Streamlit Control Center]
    end

    style H1 fill:#7b2cbf,stroke:#fff,stroke-width:2px,color:#fff
    style S1 fill:#14f195,stroke:#000,stroke-width:2px,color:#000
    style UI fill:#ff4b4b,stroke:#fff,stroke-width:2px,color:#fff
```

---

## Key Features & Visualization Modules

- **Interactive Dashboard (`research/dashboard.py`):** 

    - Centralized command center providing real-time oversight of bio-signal feeds, transaction logs, and risk-adjusted portfolio metrics.

- **Avoided Loss Metrics (`research/graph_1.py`):** 

    - Quantifies equity saved during acute market drawdowns through proactive leverage reduction.

- **Experience & Sensitivity Decay (`research/graph_2.py`):** 

    - Models dynamic thresholding over repeated stress exposure cycles to prevent premature liquidations.

- **Slippage-Adjusted Yield Comparison (`research/graph_3.py`):** 

    - Evaluates net yield performance against execution friction and rebalancing frequency.


---

## Installation & Usage

1. Prerequisites
   Ensure Python 3.8+ is installed along with the required analytical dependencies:

   `pip install pandas numpy matplotlib seaborn streamlit`

2. Running Individual Visualizations:
   
   - `python research/graph_1.py`
   - `python research/graph_2.py`
   - `python research/graph_3.py`

---

## Summary of Key Data Files

| File Name | Description | 
| --- | --- |
| final_backtest_results.csv | Time-series record of portfolio value, active leverage, and benchmark returns. |
| hormone_transaction_logs.csv | Granular order execution records with bio-circuit breaker intervention flags. |
| processed_bio_signals.csv | Normalized physiological indicators (stress proxies, cortisol scales, HRV). |
| processed_market_signals.csv | Cleaned macro volatility indicators, spread metrics, and price action data. |

---

Visual Outputs

1. **Cortisol.png**

![Cortisol-Beta Coupling](outcomes/Cortisol.png)

This graph represents the rolling correlation analysis (250-period window) between biological stress signals and portfolio leverage states over a trade sequence. With an average coupling coefficient of only 0.03, the figure proves that biological stress is largely non-correlated with external market volatility. This independence allows the Bio-Stress Index to function as a unique, non-redundant risk indicator that can signal internal emotional volatility even when market signals remain neutral.

2. **Correlation_heatmap.png**

![System Interdependency Matrix](outcomes/correlation_heatmap.png)

The illustrations represents the correlation heatmap provides a cross-variable analysis of the framework’s core metrics: Rolling Volatility, Leverage Caps, Executed Leverage, and the Bio-Stress Index. The matrix confirms the structural integrity of the system by showing near-zero or slightly negative correlations between biological stress and market volatility (-0.03). These results validate the use of the Bio-Stress Index as a pure metric for internal emotional states, distinct from external market-driven stress.

3. **final_analysis.png**

![Hormone-Responsive Logic](outcomes/final_analysis.png)

As shown in the above graph it shows the top panel of this graph shows the “Biological Circuit Breaker” in action, representing the dynamic modulation of leverage caps over time. The logic engine executes rapid transitions between risk states thus dropping leverage from a high of 10x to a defensive 1x; in direct response to detected high-stress physiological regimes. This automated dampening protects the protocol from emotional decision-making during periods of user panic.

4. **graph_1_avoided_loss.png**

![Bio-Responsive Circuit Breaker Efficiency](outcomes/graph_1_avoided_loss.png)

The above graph illustrates the real-time execution efficiency of the biological circuit breaker during simulated high-volatility events (5% market drops). The 3D scatter plot correlates 30-day rolling market volatility, inverse biometric stress levels (derived from RMSSD), and total avoided loss. The linear clustering demonstrates a flawless deterministic response from the Solana smart contract: as market volatility induces simulated physiological stress, the protocol autonomously forces leverage reductions (e.g., scaling down from 10x to 1x), successfully generating predictable capital preservation proportional to the severity of the stress trigger.

5. **graph_2_experience_decay.png**

![Experience Effect Decay](outcomes/graph_2_experience_decay.png)

This graph shows the algorithmic adjustment of baseline risk tolerance over a trader's lifecycle. By integrating a dynamic decay parameter (λ), the system mathematically weighs the impact of past macroeconomic shocks on the user's current nervous system. The graph contrasts high recency bias (λ = 3.0) against long-term financial memory (λ = 0.5). This model allows the smart contract to construct a deeply personalized, time-weighted risk profile that adjusts the portfolio's maximum allowable leverage based on the specific market traumas a user has lived through.

6. **graph_3_slippage_yield.png**

![Slippage-Adjusted Yield Comparison](outcomes/graph_3_slippage_yield.png)

This graph tracks the cumulative portfolio yield of a standard fixed-leverage strategy (10x) against the Hormone-Responsive model during a period of acute market panic. While the smart contract incurs a constant 0.1% algorithmic slippage penalty every time it dynamically scales down leverage, the graph proves this cost is negligible compared to the catastrophic drawdowns avoided. The standard portfolio is wiped out by the panic event, whereas the Bio-Responsive portfolio successfully detaches from the crash via rapid deleveraging, stabilizing the yield curve and proving the immense financial value of continuous biological risk management.

7. **graph_a_cortisol_beta.png**

![Cortisol-Beta Correlation](outcomes/graph_a_cortisol_beta.png)

Above graph shows scatter plot that illustrates the relationship between a user’s physiological state and their sustainable trading capacity. The regression line, accompanied by a 95% confidence interval, quantifies how higher levels of “Biological Calm” (measured via RMSSD) correlate with the ability to maintain higher portfolio Beta or leverage. The data suggests that as biological stress increases (lower RMSSD), the safe threshold for leverage execution decreases, providing a biological basis for risk-adjustment.

8. **mitigation_loss.png**

![Cumulative Loss Mitigation](outcomes/mitigation_loss.png)

Above graph shows the back-test that compares a Bio-Responsive Portfolio against a standard 10x fixed-leverage strategy during a simulated 12% market shock. While the standard portfolio (red) suffers instant liquidation due to over-exposure, the bio-adjusted model (green) preemptively triggers a 0.1x leverage floor, surviving the crash and successfully compounding wealth over 4,150 periods. This proves the immense financial value of integrating continuous biological feedback into decentralized solvency frameworks.

9. **panic_nominal.png**

![Nominal State](outcomes/panic_nominal.png)

The Bio-Responsive Portfolio in a nominal physiological condition is shown above. The system maintains excellent capital efficiency, enabling maximum exploitation of the trader's risk appetite, thanks to biometric sensors delivering steady HRV measurements. The model shows that it can extract maximum alpha when the decentralized solvency framework finds a stable operator by permitting dynamic leverage deployment, which maximizes profits during market growth stages without the arbitrary limits of static leverage.

10. **panic_active.png**

![Active State](outcomes/panic_active.png)

The above image illustrates the system immediately following a triggered circuit breaker event. The "Anchor Guard" algorithm overrides both automated expansion signals and manual overrides when it detects a biometric abnormality (physiological discomfort). The system successfully protects the portfolio from volatility by preemptively pivoting it to a 0.1x leverage floor. The shift from high-exposure deployment to protective solvency is captured in this image, emphasizing the platform's function as an automated insurance layer against rash decisions.
