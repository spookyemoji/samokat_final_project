#Вывести логины курьеров и количество их активных заказов
SELECT c.login, COUNT(o.id) as "OrdersCount"
FROM "Couriers" AS c
LEFT JOIN "Orders" AS o ON c.id = o."courierId"
WHERE o."inDelivery" = true
GROUP BY c.login;

#Вывести статусы заказов
SELECT track, CASE
WHEN finished = true THEN 2
WHEN cancelled = true THEN -1
WHEN "inDelivery" = true THEN 1
ELSE 0 END AS stage
FROM "Orders";