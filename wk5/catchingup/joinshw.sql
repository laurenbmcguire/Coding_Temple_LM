   
--1. List all customers who live in Texas (use JOINs)
select first_name, last_name, district
from customer
join address on address.address_id = customer.address_id
where district = 'Texas'

--2. Get all payments above $6.99 with the Customer's Full Name
select first_name, last_name, amount
from customer
join payment payment on payment.customer_id = customer.customer_id
where amount > 6.99

--3. Show all customers names who have made payments over $175(use subqueries)
select first_name, last_name, payment.customer_id, sum(amount) 
from customer
join payment on payment.customer_id = customer.customer_id
group by payment.customer_id, first_name, last_name 
having sum(amount) > 175

--4. List all customers that live in Nepal (use the city table)
select first_name, last_name, city
from customer
join address on address.address_id = customer.address_id 
join city on city.city_id = address.city_id 
where city = 'Nepal'

--5. Which staff member had the most transactions?  
select staff_id, count(payment)
from payment 
group by staff_id 

--6. How many movies of each rating are there?
select  rating, count (rating) 
from film
group by rating

--7.Show all customers who have made a single payment above $6.99 (Use Subqueries) FALTA
select first_name, last_name, payment.customer_id, amount 
from customer
join payment on payment.customer_id = customer.customer_id
group by payment.customer_id, first_name, last_name, amount 
having COUNT(payment.payment_id) = 1 and amount > 6.99

-- 8 How many free rentals did our store give away?
select COUNT(amount)
from payment 
where amount = 0
