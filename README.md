# my-flask-api

This is a simple Flask-based REST API that accepts an array of mixed data types and returns processed results including categorized numbers, alphabets, special characters, and computed summaries.

## Features

- Accepts a POST request with an array input via `/bfhl` endpoint
- Separates numbers into odd and even arrays (all numbers returned as strings)
- Extracts alphabets, converting them to uppercase
- Identifies special characters separately
- Computes the sum of all numeric elements
- Concatenates alphabetic characters in reverse order with alternating capitalization
- Returns user details (user_id, email, roll number) in response

## Installation

1. Clone the repository:
