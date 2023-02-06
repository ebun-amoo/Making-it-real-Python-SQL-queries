# Making it real

This exercise will let you practice connecting to a SQLite database from Python, executing SQL queries, and handling the results of the query. You will also practice refactoring code to use a real database instead of mock data.

## Mock Data

Mock data is dummy or placeholder data that is used in place of real data when developing or testing an application. It is often used to simulate real data when the actual data is not yet available, or when the real data is not appropriate for the current stage of development or testing.

Mock data is useful in several ways when building an application:

- Prototyping: When prototyping an application, developers often don't have real data to work with. Mock data allows developers to quickly create a functioning prototype, which can be used to get feedback from stakeholders or to test the usability of the application.
- Simulation: Mock data can be used to simulate different scenarios or edge cases that may not be possible or practical to test with real data. This can include things like testing how the application behaves under high load or when dealing with large amounts of data.
- Development speed: Using mock data can speed up the development process since developers do not need to wait for real data or do not need to go through the process of cleaning data.

In this exercise, you'll take an application that uses mock data and convert it
to one that relies actual database queries.

## Starter Code

Another developer has created a CLI interface in `main.py` to work with products. 
Right now, it uses mock data to represent the products. In `products.py`, there 
is a list called `mock_data` with dictionaries representing fake products.

Run `python main.py` to see how the CLI interface works.

Your ops team has also shared with you the actual database of products, a SQLite
database in the file `products.db`.

You can run `sqlite3 products.db` and runs some SQL queries to explore the
products database.

## Your Task

Your job is to _make it real_. You need to swap out the functions in
`products.py` with code that interacts with the database in `products.db`. When
you are finished, you should be able to delete the `mock_data` list, and the CLI
program should still work.

## Instructions

1. Modify the Python script to connect to the `products.db` database and retrieve the list of products from the `products` table. 
2. Update the script to display the products from the database, instead of the mock data.
3. Test the script to ensure that it correctly retrieves and displays the data from the products table in the database. Run `python main.py` and try out each of the CLI options.

There aren't any automated tests for this exercise. You are expected to test the
CLI yourself. If it's helpful, you can write automated tests to help you as you 
make changes to the code.

Notes: 
- you should not need to modify `main.py` -- all of the product data
    interface code is in `products.py`.
- you may find it helpful to test your queries in the sqlite console before you
    use them in `products.py`
- you may find it useful to set the `row_factory` of the connection object to
    `sqlite3.Row`, so that you can access fields by name instead of by the
    position in the tuple
