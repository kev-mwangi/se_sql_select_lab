# STEP 1A
# Import SQL Library and Pandas
import sqlite3
import pandas as pd

# STEP 1B
# Connect to the database
conn = sqlite3.connect("data.sqlite")


# STEP 2
# Replace None with your code
df_first_five = pd.read_sql_query("SELECT * FROM employees LIMIT 5", conn)

# STEP 3
# Replace None with your code
# STEP 3
df_five_reverse = pd.read_sql_query(
    """
    SELECT *
    FROM employees
    ORDER BY employeeNumber DESC
    LIMIT 5;
    """,
    conn
)

# STEP 4
# Replace None with your code
df_alias = pd.read_sql_query(
    """
    SELECT
        firstName AS first_name,
        lastName AS last_name,
        jobTitle AS job_title
    FROM employees;
    """,
    conn
)

# STEP 5
# Replace None with your code
df_executive = pd.read_sql_query(
    """
    SELECT *
    FROM employees
    WHERE jobTitle LIKE '%President%' OR jobTitle LIKE '%VP%';
    """,
    conn
)

# STEP 6
# Replace None with your code
df_name_length = pd.read_sql_query(
    """
    SELECT
        firstName,
        lastName,
        LENGTH(firstName || ' ' || lastName) AS name_length
    FROM employees;
    """,
    conn
)

# STEP 7
# Replace None with your code
df_short_title =  pd.read_sql_query(
    """
    SELECT firstName, lastName, jobTitle
    FROM employees
    WHERE LENGTH(jobTitle) <= 20;
    """,
    conn
)

# STEP 8
# Replace None with your code
sum_total_price =  pd.read_sql_query(
    """
    SELECT SUM(quantityOrdered * priceEach) AS total_price
    FROM orderdetails;
    """,
    conn
)
sum_total_price = sum_total_price.loc[0, 'total_price']

# STEP 9
# Replace None with your code
df_day_month_year = pd.read_sql_query(
    """
    SELECT
        orderNumber,
        orderDate,
        CAST(strftime('%d', orderDate) AS INTEGER) AS order_day,
        CAST(strftime('%m', orderDate) AS INTEGER) AS order_month,
        CAST(strftime('%Y', orderDate) AS INTEGER) AS order_year
    FROM orders;
    """,
    conn
)
conn.close()