--Outcome for every month, for 2019 and username jorge10
SELECT date_outcome, SUM(outcome.amount_outcome)
FROM outcome
    INNER JOIN  user
    ON outcome.ID_user=user.id 
WHERE user.username="jorge10" 
    AND outcome.amount_outcome 
    AND outcome.date_outcome1=2019
    AND outcome.currency_outcome="pln"
GROUP BY outcome.date_outcome
