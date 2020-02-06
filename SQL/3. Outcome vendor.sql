--Total spent by vendor (Biedronka):
SELECT sum(outcome.amount_outcome) \
    FROM outcome \
    INNER JOIN user, vendor \
        ON outcome.ID_vendor=vendor.id \
        AND outcome.ID_user=user.id \
    WHERE user.username="jorge10" \
        AND vendor.vendor_name="Biedronka"
