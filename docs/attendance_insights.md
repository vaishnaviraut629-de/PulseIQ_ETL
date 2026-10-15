# Attendance Trends - Insight Note (Task 4)

## 3 Findings:
1. **Monthly Trend:** April to Aug 2025 data shows consistent attendance, rolling 3-month average smooths small dips.
2. **Department:** Highest attendance count in [check summary_by_dept.csv], Lowest in [check]. HR should plan staffing accordingly. Highest dept may have shift issues.
3. **Weekday & Leave:** Weekday analysis shows typical lower attendance on Mondays/Fridays. Leave by type needs review.

## What it means + HR Action:
- If a dept is lowest, check if it's due to remote work or attrition.
- Late arrivals concentrated on Mondays -> flexible start time trial.
- Use rolling avg to forecast next month staffing.

## Limit / Not Sure:
- Data is only 5 months (Apr-Aug 2025), small sample for seasonality. Fake data may not have real festival effects.
- Anomaly file sample size small, may be AI false positives.

## December Drop - Real or Fake?
- Our current data has NO December (only Apr-Aug). So December drop seen in spec is likely effect of fake data generation (year-end leaves auto-added).
- How to check: Compare with 2+ years real data, check if Dec drop repeats every year, check HR leave policy logs, run time-series decomposition (statsmodels) to separate trend vs seasonal vs residual. If residual is high in Dec only in fake data, it's fake effect.
