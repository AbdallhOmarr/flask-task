
## creating database
def create_db():
    from app import mysql 

    print("database created")
    cursor = mysql.connection.cursor()
    query = "CREATE DATABASE car_rent_db_dev;"
    cursor.execute(query)
    cursor.close()


def create_table(table_name, columns, foreign_keys=None):
    try:
        # Build the column definitions string
        columns_str = ', '.join(f'{col[0]} {col[1]}' for col in columns)

        # Build the foreign keys string
        foreign_keys_str = '' if foreign_keys is None else f', {foreign_keys}'

        # Construct the CREATE TABLE query
        query = f'''
                    CREATE TABLE {table_name} (
                        {columns_str}
                        {foreign_keys_str}
                    );
                '''

        from app import mysql

        cursor = mysql.connection.cursor()
        cursor.execute(query)
        cursor.close()

        # Commit the changes to the database
        mysql.connection.commit()

        # Return True if the query is executed successfully
        return True
    except Exception as e:
        # If an exception occurs, print the error and return False
        print(f"Error: {e}")
        return False
