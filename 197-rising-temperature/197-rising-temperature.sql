# Write your MySQL query statement below

SELECT W1.id from Weather W1, Weather W2
where W1.temperature > W2.temperature and Datediff(W1.recordDate, W2.recordDate) = 1;


# select wt2.id 
# from Weather wt1, Weather wt2
# where wt2.temperature > wt1.temperature and
# 	to_days(wt2.recordDate) - to_days(wt1.recordDate) = 1;