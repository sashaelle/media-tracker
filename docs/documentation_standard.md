# Personal Media Tracker

### Documentation Standard

The purpose fo this documentation standard is to keep all files and functions consistent.
It also ensures the use of @pre and @post, as required by Professor Gupta.

## File Documentation

Each Python file must begin with a file header comment that includes:

- File Name
- Project Name
- Author(s)
- Brief Description of the file's purpose

Example:

    """
    File: database.py
    Project: Personal Media Tracker
    Author(s): Sasha Crawford

    Description: Provides database creation.
    """

## Function Documentation

Each function must have a docstring directly below the function definition.
The docstring must contain:

- A brief description
- Args
- Returns
- @pre
- @post

Example:

    """
    Function name: search()
    Purpose: Searches the media catalog for titles that match the user input.
    Args:
        title (str): The title entered by the user.
    Returns:
        list: A list of matching media records.

    @pre: The database connection must be established and title must be a non-empty string.
    @post: A list of matching results is returned. If no matches are found, an empty list is returned.
    """

## @pre and @post

@pre describes the preconditions of the function.
These are the conditions that must be that must be true before the execution of the function.

@post describes the post conditions of the function.
These are the conditions that will be true after the function finishes.
