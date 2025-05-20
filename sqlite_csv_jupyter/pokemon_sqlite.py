import pandas as pd
import sqlite3

def csv_to_sqlite(csv_file, db_file):
    # Load the CSV file into a DataFrame
    df = pd.read_csv(csv_file)

    # Connect to the SQLite database (it will be created if it doesn't exist)
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # Create a table with the same column names as the CSV file
    columns = ", ".join([f'"{col}" TEXT' for col in df.columns])
    create_table_query = f"CREATE TABLE IF NOT EXISTS pokemon ({columns});"
    cursor.execute(create_table_query)

    # Insert data into the table
    df.to_sql('pokemon', conn, if_exists='replace', index=False)

    # Commit changes and close the connection
    conn.commit()
    conn.close()

# Usage
csv_to_sqlite('pokemon.csv', 'pokemon.db')
