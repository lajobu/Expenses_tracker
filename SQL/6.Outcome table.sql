--Outcomes introduces in Dec 2019, with category name and vendor name
SELECT outcome.amount_outcome, outcome.currency_outcome,
    category.category_name, vendor.vendor_name
FROM outcome
INNER JOIN category, vendor, user
    ON outcome.ID_category=category.id
    AND outcome.ID_vendor=vendor.id
    AND outcome.ID_user=user.id
WHERE user.id=10
    AND outcome.date_outcome="Dec"
    AND outcome.date_outcome1=2019
