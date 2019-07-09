import psycopg2

DBNAME = "news"

request_1 = "What are the most popular articles of all time?"

query_1 = ("SELECT title, count(*) as views FROM articles \n"
           "  JOIN log\n"
           "    ON articles.slug = substring(log.path, 10)\n"
           "    GROUP BY title ORDER BY views DESC LIMIT 3;")

request_2 = "Who are the most popular article authors of all time?"

query_2 = ("SELECT authors.name, count(*) as views\n"
           "    FROM articles \n"
           "    JOIN authors\n"
           "      ON articles.author = authors.id \n"
           "      JOIN log \n"
           "      ON articles.slug = substring(log.path, 10)\n"
           "      WHERE log.status LIKE '200 OK'\n"
           "      GROUP BY authors.name ORDER BY views DESC;")

request_3 = "On which days did more than 1% of the requests lead to errors?"

query_3 = ("SELECT day, perc from("
          "SELECT day, round((sum(requests)/(select count(*) from log where "
          "substring(cast(log.time as text), 0, 11) = day) * 100), 2) as "
          "perc from (select substring(cast(log.time as text), 0, 11) as day, "
          "count(*) as requests from log where status like '%404%' group by day)"
          "as log_percentage group by day order by perc desc) as final_query "
          "where perc >= 1")

# Connect to the database and feed query to extract results


def get_queryResults(sql_query):
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(sql_query)
    results = c.fetchall()
    db.close()
    return results

result1 = get_queryResults(query_1)
result2 = get_queryResults(query_2)
result3 = get_queryResults(query_3)


# Create a function to print query results


def print_results(query_list):
    for i in range(len(query_list)):
        title = query_list[i][0]
        res = query_list[i][1]
        print("\t" + "%s - %d" % (title, res) + " views")
    print("\n")

print(request_1)
print_results(result1)
print(request_2)
print_results(result2)
print(request_3)
print_results(result3)
