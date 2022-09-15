# Please write a DELETE statement and DO NOT write a SELECT statement.
# Write your MySQL query statement below

# DELETE from Person where id not in (SELECT min(id) from Person GROUP BY email)

# GROUP BY email ASC

DELETE p1 from Person p1, Person p2 where p1.email=p2.email and p1.id>p2.id