
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



def select_data_table(table_name,columns='*',filters=None):
    try:
        from app import mysql

        cursor = mysql.connection.cursor()
        
        # Build the column definitions string
        columns_str = ', '.join(f'{col}' for col in columns)

        if filters!=None:
            filter_str = 'WHERE ' + ' OR '.join(f'{col[0]} = "{col[1]}"' for col in filters)
        else:
            filter_str = ''
            
            
        query = f'''
                    SELECT {columns_str} FROM {table_name} 
                    {filter_str}  
                ''' 
                
        print(query)
        cursor.execute(query)
        results= cursor.fetchall()
        cursor.close()

        # Return results if the query is executed successfully
        return results
    except Exception as e:
        # If an exception occurs, print the error and return False
        print(f"Error: {e}")
        return False



def update_data_table(table_name,filters,columns):
    try:
        from app import mysql

        cursor = mysql.connection.cursor()
        print("cursor created")
        print(columns)
        values_str = 'SET ' + ' , '.join(f'{col[0]} = "{col[1]}"' for col in columns)
        print(f"values:{values_str}")

        filter_str = 'WHERE ' + ' OR '.join(f'{col[0]} = "{col[1]}"' for col in filters)
        
        print(f"filters:{filter_str}")

        query = f'''
                    UPDATE {table_name}
                    {values_str}
                    {filter_str}
                ''' 
                
        print(f"query:{query}")
        cursor.execute(query)
        # Commit the changes to the database
        mysql.connection.commit()

        cursor.close()

        # Return results if the query is executed successfully
        return True
    except Exception as e:
        # If an exception occurs, print the error and return False
        print(f"Error: {e}")
        return False


def add_data_table(table_name,columns,values):
    try:
        from app import mysql

        cursor = mysql.connection.cursor()
        
        columns_str = ' , '.join(f'{col}' for col in columns)

        values_str = ' , '.join(f'"{col}"' for col in values)
            
            
        query = f'''
                    INSERT INTO {table_name} ({columns_str})
                    VALUES ({values_str});
                ''' 
                
        print(query)
        cursor.execute(query)
        # Commit the changes to the database
        mysql.connection.commit()

        cursor.close()

        # Return results if the query is executed successfully
        return True
    except Exception as e:
        # If an exception occurs, print the error and return False
        print(f"Error: {e}")
        return False
    
    
    
def delete_data_table(table_name,id):
    try:
        from app import mysql

        cursor = mysql.connection.cursor()
                  
            
        query = f'''
                    DELETE FROM {table_name}
                    WHERE id = "{id}";
                ''' 
                
        print(query)
        cursor.execute(query)
        # Commit the changes to the database
        mysql.connection.commit()

        cursor.close()

        return True
    except Exception as e:
        # If an exception occurs, print the error and return False
        print(f"Error: {e}")
        return False

