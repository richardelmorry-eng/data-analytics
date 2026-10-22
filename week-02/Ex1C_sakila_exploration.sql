/*
a) The actor table has each actor's actor_id, first_name, last_name, and the last_update time.
b) The film table has details about each film, including film_id, title, description, release_year, language_id, rental_duration, rental_rate, length, replacement_cost, rating, special_features, and last_update.
c) The film_actor table contains both actor_id and film_id.
d) The rental table records each rental with the rental_date, inventory_id, customer_id, return_date, staff_id, and last_update. It is hard to read because it only has ID numbers instead of film titles or customer names.
e) The inventory table has inventory_id, film_id, store_id, and last_update, so it shows which copy of which film is held at which store.
f) You need the rental, inventory, and film tables. The rental table has the rental_date and the inventory_id, the inventory table connects each inventory_id to a film_id, and the film table connects each film_id to the film title.
*/

SELECT rental_id, rental_date, inventory_id FROM rental;
SELECT inventory_id, film_id FROM inventory;
SELECT film_id, title FROM film;