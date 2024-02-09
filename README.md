# Python-Data-Pipeline
This project is an ETL (Extract, Transform, Load) pipeline designed to transfer data from a MySQL database to a PostgreSQL database. It consists of several Python scripts for reading data from MySQL, transforming it, and writing it to PostgreSQL.

## Installation

1. Clone the repository to your local machine:
   ```
   git clone <repository_url>
   ```
   Replace `<repository_url>` with the URL of your GitHub repository.

2. Install the required dependencies using pip:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Ensure that you have MySQL and PostgreSQL databases set up with the appropriate schemas.

2. Modify the `config.py` file with the database connection details for both MySQL and PostgreSQL.

3. Run the `main.py` script to execute the ETL process:
   ```
   python main.py
   ```

4. Monitor the progress and check the `etl.log` file for any errors or informational messages.

## Files

- `read.py`: Contains functions for reading data from MySQL tables.
- `write.py`: Contains functions for writing data to PostgreSQL tables.
- `util.py`: Contains utility functions for database connections and logging.
- `app.py`: Main script to orchestrate the ETL process.
- `config.py`: Configuration file with database connection details.
- `requirements.txt`: List of Python dependencies required for the project.
- `etl.log`: Log file to store information and errors during the ETL process.

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

