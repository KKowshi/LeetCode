# Write your MySQL query statement below
-- SELECT p.product_id,
-- IFNULL(ROUND(SUM(units*price)/SUM(units),2),0) AS average_price
-- FROM Prices p
-- LEFT JOIN UnitsSold u
-- ON u.product_id = p.product_id
-- WHERE purchase_date >= start_date AND purchase_date <= end_date
-- GROUP BY p.product_id

# Write your MySQL query statement below
SELECT p.product_id, IFNULL(round(SUM(p.price*u.units)/sum(u.units),2),0) as average_price
FROM Prices p 
LEFT JOIN UnitsSold u
ON p.product_id = u.product_id AND 
u.purchase_date BETWEEN p.Start_date and p.end_date
GROUP BY p.product_id
