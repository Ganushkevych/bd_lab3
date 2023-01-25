import psycopg2
import matplotlib.pyplot as plt

username = 'postgres'
password = 'postgres'
database = 'postgres'
host = 'localhost'
port = '5432'

query_1 = '''
CREATE VIEW IssueCountByRating AS
SELECT TRIM(issue_title) as issue_title, TRIM(rating) as rating
FROM issue_new, info_new
WHERE issue_new.info_id = info_new.info_id
ORDER BY rating
'''

query_2 = '''
CREATE VIEW IssueCountByPrice AS
SELECT TRIM(issue_title) as issue_title, price
FROM issue_new, info_new
WHERE issue_new.info_id = info_new.info_id
ORDER BY price
'''

query_3 = '''
CREATE VIEW IssueCountByImprint AS
SELECT TRIM(issue_title) as issue_title, TRIM(imprint) as imprint
FROM issue_new, authors_new
WHERE issue_new.authors_id = authors_new.authors_id
ORDER BY imprint desc
'''

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

with conn:
    cur1 = conn.cursor()

    print('1. \n')
    cur1.execute('DROP VIEW IF EXISTS IssueCountByRating')
    cur1.execute(query_1)
    cur1.execute('SELECT * FROM IssueCountByRating')

    X = []
    Y = []
    for row in cur1:
        X.append(row[0])
        Y.append(row[1])

    x_range = range(len(X))

    figure, (bar_ax, pie_ax, graph_ax) = plt.subplots(1, 3)
    bar = bar_ax.bar(x_range, Y, width = 0.5)
    bar_ax.set_title('Кількість випусків по різним рейтингам')
    bar_ax.set_xlabel('Випуск')
    bar_ax.set_ylabel('Рейтинг')
    #bar_ax.set_xticks(x_range)
    #bar_ax.set_xticklabels(X)

print()
with conn:
    cur2 = conn.cursor()

    print('2. \n')
    cur2.execute('DROP VIEW IF EXISTS IssueCountByPrice')
    cur2.execute(query_2)
    cur2.execute('SELECT * FROM IssueCountByPrice')

    X = []
    Y = []
    for row in cur2:
        X.append(row[0])
        Y.append(row[1])

    pie_ax.pie(Y, labels=X, autopct='%1.1f%%', textprops={'fontsize': 1}, rotatelabels=True)
    pie_ax.set_title('Кількість випусків по різних цінах')


print()
with conn:
    cur3 = conn.cursor()

    print('3. \n')
    cur3.execute('DROP VIEW IF EXISTS IssueCountByImprint')
    cur3.execute(query_3)
    cur3.execute('SELECT * FROM IssueCountByImprint')

    X = []
    Y = []
    for row in cur3:
        X.append(row[0])
        Y.append(row[1])

    #plt.plot(Y, X) 
    #plt.title('Кількість випусків за видавництвами') Замінив на стовпчикову, оскільки на цій надто багато тексту
    figure, (bar_ax, pie_ax, graph_ax) = plt.subplots(1, 3)
    bar1 = bar_ax.bar(x_range, Y, width = 0.5)
    bar_ax.set_title('Кількість випусків по різним видавництвам')
    bar_ax.set_xlabel('Випуск')
    bar_ax.set_ylabel('Рейтинг')
    plt.show()


mng = plt.get_current_fig_manager()
mng.resize(1400, 600)