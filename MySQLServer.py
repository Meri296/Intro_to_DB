#!/usr/bin/env python3
# File: MySQLServer.py
"""
Script to create the 'alx_book_store' database in MySQL.
If the database already exists, it won't cause an error.
"""

import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL server (adjust user/password/host to your setup)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",        # Replace with your MySQL username
            password="password" # Replace with your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # Create database if it doesn't exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error: Unable to connect or create database. Details: {e}")

    finally:
        # Close cursor and connection
        if 'cursor' in locals() and cursor:
            cursor.close()
        if connection.is_connected():
            connection.close()

if __name__ == "__main__":
    create_database()
