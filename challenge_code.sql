-- (https://8weeksqlchallenge.com/case-study-1/ - Q7. to Q8. of case study): 

CREATE database dannys_diner;

CREATE TABLE sales (
  customer_id VARCHAR(1),
  order_date DATE,
  product_id INTEGER
);

INSERT INTO sales
  (customer_id, order_date, product_id)
VALUES
  ('A', '2021-01-01', '1'),
  ('A', '2021-01-01', '2'),
  ('A', '2021-01-07', '2'),
  ('A', '2021-01-10', '3'),
  ('A', '2021-01-11', '3'),
  ('A', '2021-01-11', '3'),
  ('B', '2021-01-01', '2'),
  ('B', '2021-01-02', '2'),
  ('B', '2021-01-04', '1'),
  ('B', '2021-01-11', '1'),
  ('B', '2021-01-16', '3'),
  ('B', '2021-02-01', '3'),
  ('C', '2021-01-01', '3'),
  ('C', '2021-01-01', '3'),
  ('C', '2021-01-07', '3');
 

CREATE TABLE menu (
  product_id INTEGER,
  product_name VARCHAR(5),
  price INTEGER
);

INSERT INTO menu
  (product_id, product_name, price)
VALUES
  ('1', 'sushi', '10'),
  ('2', 'curry', '15'),
  ('3', 'ramen', '12');
  

CREATE TABLE members (
  customer_id VARCHAR(1),
  join_date DATE
);

INSERT INTO members
  (customer_id, join_date)
VALUES
  ('A', '2021-01-07'),
  ('B', '2021-01-09');
  
 -- Note: all of the answers should be provided in a single query 
-- Q7. Items 1 and 2
SELECT c.product_id FROM sales c INNER JOIN members d ON c.customer_id = d.customer_id WHERE c.order_date < d.join_date;

-- Q8. Customer A purchases 2 items with total price of 25. 
-- Customer B purchases 3 items with total price of 40. 
SELECT c.customer_id, COUNT(e.product_id), SUM(e.price) FROM menu e INNER JOIN sales c ON c.product_id = e.product_id INNER JOIN members d ON c.customer_id = d.customer_id WHERE c.order_date < d.join_date GROUP BY c.customer_id; 
