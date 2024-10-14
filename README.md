# Tip Processor

This is a small script to help scan a Starbucks tip report.

## The Problem

When counting and distributing the tips, we get a printed tip report.  I want to import it into a spreadsheet, but even using Google Lens to copy/paste the text, I got all the data in a single column instead of a column for store number, partner number, name, and hours.  Sorting it all manually would take less time than just typing it all in.  But sometimes, typing manually I would miss people which causes all kinds of problems.

## The Solution

This script will take all that data and sort it into the proper columns.  It expects a .txt file with only the data for the columns we care about: don't copy in any of the headers like the date or when the report was run.  Make sure every piece of data is on a separate line.  If the store number and partner name are on the same line the script will throw an error.  Once the file is formatted correctly, just run the included script and include the filename

```bash

./convert.sh report.txt

```

and the program will run and tell you that the report was saved in a file with the current date and time.

## Setup

Make sure Python is installed and run `./setup.sh` and the requirements will be installed.

This was written in Linux, so it probably won't work properly in Windows or Mac.  I can give detailed instructions if anybody wants them.
