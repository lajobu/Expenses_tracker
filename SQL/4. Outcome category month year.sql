--Total spent by month, year, category (parties):
SELECT SUM(outcome.amount_outcome)
    FROM outcome
    INNER JOIN CATEGORY
        ON outcome.ID_category = category.id
    WHERE outcome.ID_user=10
        AND category.category_name= "Parties"
        AND outcome.date_outcome="Dec"
        AND outcome.date_outcome1="2019"
        AND outcome.currency_outcome="pln"
