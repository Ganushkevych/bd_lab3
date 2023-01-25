import psycopg2

username = 'postgres'
password = 'postgres'
database = 'postgres'

query_1 = '''
CREATE TABLE authors_new
(
	authors_id       int     NOT NULL,
	writer  char(100)	NULL,
	penciler    char(100)	NULL,
	cover_artist	char(100)	NULL,
	imprint		char(50)	NULL,
    CONSTRAINT pk_authors_new PRIMARY KEY (authors_id)
);
'''

query_2 = '''
CREATE TABLE issue_new
(
	issue_id	INT		NOT NULL,
	issue_title		char(100)	NULL,
	authors_id       INT       NOT NULL,
	info_id       INT       NOT NULL,
    CONSTRAINT pk_issue_new PRIMARY KEY (issue_id)
);
'''

query_3 = '''
CREATE TABLE info_new
(
	info_id		INT  NOT NULL,
	comic_name		char(200)	NULL,
	active_years	char(50)	NULL,
	publish_date	char(50)	NULL,
	format		char(50)	NULL,
	rating		char(50)	NULL,
	price		float	NULL,
    CONSTRAINT pk_info_new PRIMARY KEY (info_id)
);
'''


conn = psycopg2.connect(user=username, password=password, dbname=database)

cur = conn.cursor()

with open('C:/Users/админ/Desktop/MCA.csv', 'r') as f1:
    cur.execute('DROP TABLE authors_new')
    cur.execute(query_1)
    next(f1)
    cur.copy_from(f1, 'authors_new', sep=';')
conn.commit()

with open('C:/Users/админ/Desktop/MCI.csv', 'r') as f2:
    cur.execute('DROP TABLE issue_new')
    cur.execute(query_2)
    next(f2)
    cur.copy_from(f2, 'issue_new', sep=';')
conn.commit()

with open('C:/Users/админ/Desktop/MCIN.csv', 'r') as f3:
    cur.execute('DROP TABLE info_new')
    cur.execute(query_3)
    next(f3)
    cur.copy_from(f3, 'info_new', sep=';')
conn.commit()
