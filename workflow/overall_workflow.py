# @BEGIN Overall_Data_Cleaning
# @IN Farmers_latest_csv  @URI file://Data/Farmers_latest.csv

    # @BEGIN CleanWithOpenRefine @DESC Use OpenRefine to clean Farmers_latest.csv
    # @IN Farmers_latest_csv  @URI file://Data/Farmers_latest.csv
    # @OUT Farmers_Market_Data_csv  @URI file://Data/Farmers_Market_Data.csv
    # @END CleanWithOpenRefine

    # @BEGIN ConvertToDatabaseWithSQLite @DESC Convert csv file to db file
    # @IN Farmers_Market_Data_csv @URI file://Data/Farmers_Market_Data.csv
    # @OUT Farmers_Market_Data_db @URI file://sqlite/Farmers_Market_Data.db
    # @END ConvertToDatabaseWithSQLite

    # @BEGIN IntegrityCheckWithSQLite @DESC Use SQLite to check integrity
    # @IN Farmers_Market_Data_db @URI file://sqlite/Farmers_Market_Data.db
    # @END IntegrityCheckWithSQLite

    # @BEGIN CleanWithSQLite @DESC Clean and update database file
    # @IN Farmers_Market_Data_db @URI file://sqlite/Farmers_Market_Data.db
    # @OUT Farmers_Market_Data_sql_csv @URI file://Data/Farmers_Market_Data_sql.csv
    # @END CleanWithSQLite

# @OUT Farmers_Market_Data_sql_csv @URI file://Data/Farmers_Market_Data_sql.csv
# @END Overall_Data_Cleaning
