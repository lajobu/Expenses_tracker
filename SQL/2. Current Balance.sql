--Current balance:
SELECT (val1 - val2)
    FROM (SELECT ID_user, currency_income, sum(amount_income) AS val1
        FROM income
        GROUP BY ID_user) inc
    JOIN (SELECT ID_user, currency_outcome, sum(amount_outcome) AS val2
        FROM outcome
        GROUP BY ID_user) out
    ON (inc.ID_user = out.ID_user)
    WHERE out.ID_user = 10
        AND out.currency_outcome = "pln"
        AND inc.currency_income = "pln"