--Average spent by category (rent), with round of two decimals:
SELECT ROUND(AVG(outcome.amount_outcome), 2)
FROM outcome
WHERE outcome.ID_category=25
    AND outcome.currency_outcome="pln"