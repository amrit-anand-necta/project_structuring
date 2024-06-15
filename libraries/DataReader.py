from libraries import ConfigReader

# defining Customers Schema
def get_customers_schema():
    schema = 'customer_id int, customer_fname string, customer_lname string, username string, password string, address string, city string, state string, pincode string'
    return schema

# creating Customers Dataframe
def read_customers(spark, env):
    conf = ConfigReader.get_app_config(env)
    customers_file_path = conf['customers.file.path']
    return  spark.read \
    .format('csv') \
    .option('header', True) \
    .schema(get_customers_schema()) \
    .load(customers_file_path)

# defining Orders Schema
def get_orders_schema():
    schema = 'order_id int, order_date string, customer_id int, order_status string'
    return schema

# creating Orders Dataframe
def read_orders(spark, env):
    conf = ConfigReader.get_app_config(env)
    orders_file_path = conf['orders.file.path']
    return  spark.read \
    .format('csv') \
    .option('header', True) \
    .schema(get_orders_schema()) \
    .load(orders_file_path)