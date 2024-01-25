import sqlite3

class Karakterbog:
    def __init__(self):
        self.karakterer = []
        try:
            self.conn = sqlite3.connect('karakterbog.db')  # Connect to the SQLite database
            self.cursor = self.conn.cursor()
            # Create a table if it doesn't exist
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS statistik (
                    id INTEGER PRIMARY KEY,
                    max_karakter REAL,
                    min_karakter REAL,
                    gennemsnit_karakter REAL
                )
            """)
            self.conn.commit()  # This isn't an SQL command, but it's related to SQL operations. In SQLite, changes to the database (like creating a table or inserting data) aren't saved immediately when you execute the SQL command. They're saved when you commit the transaction. If you don't commit the transaction, the changes will be lost when your program ends.
            print("Database connected and table created successfully.")
        except Exception as e:
            print(f"Error occurred: {e}")

    def indtast_karakter(self, karakter):
        if 0 <= karakter <= 12:
            self.karakterer.append(karakter)
        else:
            return "Fejl: Karakteren skal være et decimaltal mellem 0 og 12."

    def beregn_statistik(self):
        if not self.karakterer:
            return "Ingen karakterer indtastet endnu."

        max_karakter = max(self.karakterer)
        min_karakter = min(self.karakterer)
        gennemsnit_karakter = sum(self.karakterer) / len(self.karakterer)

        # Insert the statistics into the database
        self.cursor.execute("""
            INSERT INTO statistik (max_karakter, min_karakter, gennemsnit_karakter)
            VALUES (?, ?, ?)
        """, (max_karakter, min_karakter, gennemsnit_karakter))
        self.conn.commit()  # Commit the changes

        statistik = f"Højeste karakter: {max_karakter}\nLaveste karakter: {min_karakter}\nGennemsnitlig karakter: {gennemsnit_karakter:.2f}"
        return statistik

    def clear_karakterer(self):
        self.karakterer.clear()


