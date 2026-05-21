CREATE TABLE holidays (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) UNIQUE,
    holiday_date DATE,
    public_holiday BOOLEAN,
    country VARCHAR(10)
);

SELECT COUNT(*)
FROM holidays
WHERE public_holiday=1;

SELECT holiday_month,count(*)
FROM (SELECT name,
 EXTRACT(MONTH FROM holiday_date) as holiday_month 
FROM holidays)t
GROUP BY holiday_month;

SELECT day_week,COUNT(*)
FROM(
SELECT name,
dayname(holiday_date) as day_week
FROM holidays)t
WHERE day_week IN ('Saturday','Sunday')
GROUP BY day_week;

SELECT name 
FROM(SELECT name,EXTRACT(day FROM holiday_date) as holiday_day, 
EXTRACT(month FROM holiday_date) as holiday_month,
RANK() OVER(PARTITION BY EXTRACT(month FROM holiday_date) ORDER BY EXTRACT(day FROM holiday_date) ASC) as rnk
FROM holidays
)t
where rnk=1


