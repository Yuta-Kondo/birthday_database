# Birthday Database Manager

This Python application manages a database of birthday records. It allows you to add, list, update, and delete birthday records in a PostgreSQL database through a command-line interface.

## Setup Instructions

### Prerequisites

- Python 3.x
- PostgreSQL
- `psycopg2` Python package

### Installation Steps

1. **Clone the Repository**:
   - Clone this repository to your local machine, or download the `.py` file directly.

2. **Install Python Dependencies**:
   - Install the required Python packages by running:
     ```bash
     pip install psycopg2
     ```

3. **Set Up Your PostgreSQL Database**:
   - Ensure PostgreSQL is installed and running on your machine.
   - Create a database for storing the birthday records.
   - Note down your database name, user, password, and host.

4. **Configure the Application**:
   - Open the Python script in a text editor.
   - Update the database connection parameters (`DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`) with your actual PostgreSQL database details.

5. **Create the Table**:
   - In your PostgreSQL database, create a table with the following SQL command:
     ```sql
     CREATE TABLE birthdays (
         id SERIAL PRIMARY KEY,
         name VARCHAR(100) NOT NULL,
         birth_month INTEGER NOT NULL,
         birth_day INTEGER NOT NULL,
         birth_year INTEGER
     );
     ```

## How to Use

Run the Python script with the following command-line arguments to manage your birthday database:

1. **Adding a Birthday Record**:
   - To add a new birthday record, use the following command:
     ```shell
     python birthday.py add --name "Name" --month MM --day DD --year YYYY
     ```
   - Replace `Name`, `MM`, `DD`, and `YYYY` with the person's name, birth month, day, and year. The year is optional.

2. **Listing All Records**:
   - To list all the birthday records, use the following command:
     ```shell
     python birthday.py list
     ```

3. **Updating a Birthday Record**:
   - To update an existing record, use the following command:
     ```shell
     python birthday.py update --name "Name" --month MM --day DD --year YYYY
     ```
   - Provide the new date details to update an existing record.

4. **Deleting a Birthday Record**:
   - To delete a birthday record, use the following command:
     ```shell
     python birthday.py delete --name "Name"
     ```
   - Deletes the record of the specified person.

5. **Help**:
   - For help and information about the commands, use the following command:
     ```shell
     python birthday.py --help
     ```
