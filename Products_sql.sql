-- SQLite
Select name, price, quantity, status, category
FROM Products as P
JOIN Category as C ON P.id_category = C.id
Join Status as S ON P.id_status = S.id