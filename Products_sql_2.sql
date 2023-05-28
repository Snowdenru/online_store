-- SQLite
-- Delete From Products

Select * from Products
JOIN Status ON Products.id_status = Status.id
Where price > 2000 and Status.status = 'Repaired' and quantity > 10