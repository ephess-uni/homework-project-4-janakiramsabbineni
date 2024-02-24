# hp_4.py

from datetime import datetime, timedelta
from csv import DictReader, DictWriter
from collections import defaultdict

def reformat_dates(old_dates):
    """Accepts a list of date strings in format yyyy-mm-dd, re-formats each
    element to a format dd mmm yyyy--01 Jan 2001."""
    pass  # Implement this function

def date_range(start, n):
    """For input date string `start`, with format 'yyyy-mm-dd', returns
    a list of `n` datetime objects starting at `start` where each
    element in the list is one day after the previous."""
    pass  # Implement this function

def add_date_range(values, start_date):
    """Adds a daily date range to the list `values` beginning with
    `start_date`.  The date, value pairs are returned as tuples
    in the returned list."""
    pass  # Implement this function

def fees_report(infile, outfile):
    """Calculates late fees per patron id and writes a summary report to
    outfile."""
    pass  # Implement this function

# The following main selection block will only run when you choose
# "Run -> Module" in IDLE.  Use this section to run test code.
if __name__ == '__main__':
    # You can add test code here to check the functionality of your functions
    pass
