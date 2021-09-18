# flashback-scraper

scraper for flashback.org to download all posts in a thread

usage: 
```console
PS C:\dev\Python\flashback-scraper\src> python .\main.py scrape thread {{THREAD_ID}} --output-path ../output.ndjson --sleep_ms 0.4
```

It will output JSON entries for each post, delimited by newline.

The scraper process is recoverable, if the script fails due to rate limit or other errors (will most likely happen), 
then you can rerun the script with the same output file. It will find the last sucessfully scraped page & start from there, and make sure no duplicates occur.

# Todo

* Handle posts that have been changed somehow
* Make simple client for viewing the output & search.