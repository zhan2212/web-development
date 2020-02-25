class: center, middle

# MPCS 52553-2: Web Development
## Week 3: Server-Side Rendering with the LAMP Stack
---

class: agenda

# HTTP
- CRUD operations, URL parameters, forms and validation
- The Network tab

# Sever-Side Rendering with the LAMP Stack
- PHP scripting, environment variables

# Databases
- SELECT and INSERT
- JOIN
---

# HTTP

![Google Interview Question](google_interview.png "Screenshot of Glassdoor.com")

???

For a long time, a popular interview question at Google was "What happens when
you type google.com into your browser and hit enter?" I got it myself during
onsite interviews there in 2013.

Much of the answer is about HTTP
---

# HTTP

> The **Hypertext Transfer Protocol** (**HTTP**) is an application protocol for
distributed, collaborative, hypermedia information systems.[1] HTTP is the
foundation of data communication for the World Wide Web, where hypertext
documents include hyperlinks to other resources that the user can easily access,
for example by a mouse click or by tapping the screen in a web browser.
([Wikipedia](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol))

[HTTP (Mozilla Documentation)](https://developer.mozilla.org/en-US/docs/Web/HTTP)

[How Browsers Work](https://www.html5rocks.com/en/tutorials/internals/howbrowserswork/)
---

# HTTP

Textbook: [HTTP: Learn Your Browser's Language](https://wizardzines.com/zines/http/)
by Julia Evans ([@b0rk](https://twitter.com/b0rk))

- Requests & URLs
- Headers
- Request Methods
- Responses and Status Codes
---

# Lab: HTTP Exercises
### From Learn Your Browser's Language, p. 26

`curl` - [cURL (Wikipedia)](https://en.wikipedia.org/wiki/CURL)
---

# Web Servers: Apache

> The Apache HTTP Server ("httpd") was launched in 1995 and it has been the most
popular web server on the Internet since April 1996. It has celebrated its 20th
birthday as a project in February 2015. ([httpd.apache.org](https://httpd.apache.org/))

The web server running at http://mpcs52553-2.com/ is Apache. By default, when it
receives an HTTP request, it looks for files on the local filesystem that match
the URL path and returns them to the web browser.

![httpd.pache.org](apache.png "Screenshot of httpd.apache.org")
---

# Server-Side Rendering with PHP

```html
<html>
<head>
  <title>PHP Math Examples</title>
  <link rel="stylesheet" type="text/css" href="css/style.css">
</head>
<body>
  <h1>Let's do some math on the server!</h1>
  <p>2 + 2 = <?php echo 2+2 ?></p>
  <p>8 - 3 = <?php echo 8-3 ?></p>
  <p>6 * 7 = <?php echo 6*7 ?></p>
  <p>pi = <?php echo pi()?></p>
</body>
```

Take a look at how math.php (above) renders on
[http://mpcs52553-2.com/math.php](http://mpcs52553-2.com/math.php).

???

Before the server passes math.php to the browser, it evaluates the code in the
`<?php ?>` tags. If you View Source, you'll see that they have been replaced
with plain text. Importantly, that evaluation happens on the server, before any
data is sent to the user.
---

# Server-Side Rendering with PHP

[PHP](https://www.php.net/) is a whole, Turing-complete programming language.
Famously, Facebook is written using it. We also use it extensively at my day
job.

So a web server isn't just a program that shows existing html documents to
users; it can be any arbitrarily complex program that returns HTTP responses.

![php.net](php.png "Screenshot of php.net")
---

# Lab: Server-Side Rendering

Copy the `<yourname>.html` file you uploaded to `http://mpcs52553-2.com/helloclass/`
in Week 1 and rename the copy `<yourname>.php`

Add some expressions to be evaluated server-side inside `<?php ?>` tags.
- Use `rand` ([https://www.php.net/rand](https://www.php.net/rand)) to generate
a random number. Refresh the page to see the number change.
- Use `getenv` ([https://www.php.net/getenv](https://www.php.net/getenv)) to get
the value of `HTTP_USER_AGENT` and tell you what browser is visiting the page.

Upload the result again with:
```bash
scp <yourname>.php student@mpcs52553-2.com:/var/www/html/helloclass
```

The password is `webdevelopment`
---

# The LAMP Stack

One very popular thing you might want to do with your program that responds to
HTTP requests is have it interact with a database. And for a long time the most
popular such configuration of these pieces was the
[LAMP](https://en.wikipedia.org/wiki/LAMP_(software_bundle) stack.

![LAMP Stack diagram](lamp_architecture.png "LAMP Architecture Diagram")

???

> Originally popularized from the phrase "Linux, Apache, MySQL, and PHP", the acronym "LAMP" now refers to a generic software stack model. The modularity of a LAMP stack may vary, but this particular software combination has become popular because it is sufficient to host a wide variety of web site frameworks, such as WordPress. The components of the LAMP stack are present in the software repositories of most Linux distributions.
https://en.wikipedia.org/wiki/LAMP_(software_bundle)

---

# Lab: Working with Form Submissions

[Dealing with Forms (PHP Documentation)](https://www.php.net/manual/en/tutorial.forms.php)

[http://mpcs52553-2.com/post.php](http://mpcs52553-2.com/post.php)

[http://mpcs52553-2.com/post_no_escape.php](http://mpcs52553-2.com/post_no_escape.php)
---

# Databases

[MySQL (Wikipedia)](https://en.wikipedia.org/wiki/MySQL)

[MariaDB (MariaDB Documentation)](https://mariadb.org/documentation/)

[Introduction to Relational Databases (MariaDB Documentation)](https://mariadb.com/kb/en/introduction-to-relational-databases/)

[A MariaDB Primer](https://mariadb.com/kb/en/a-mariadb-primer/)

![Database Tables](tables.png "Visualization of two Database Tables")
---

# Databases: Show and Describe

`use db;`

`show tables;`

`describe posts;`

`describe comments;`
---

# Databases: Select and Insert

`select * from posts;`

`select * from comments;`
---

# Databases: JOIN

[SQL Joins](https://www.w3schools.com/sql/sql_join.asp)

[Joins in MariaDB](https://mariadb.com/kb/en/joining-tables-with-join-clauses/)
---

# Accessing the Database with PHP

[Connecting to the Database](https://www.w3schools.com/php/php_mysql_connect.asp)

[Prepared Statements to Send Queries](https://www.php.net/manual/en/pdo.prepared-statements.php)
---

# Lab: Exercise 3

[A Web Journal](http://mpcs52553-2.com/weblog.php)

[Exercise 3 on GitLab](https://mit.cs.uchicago.edu/trevoraustin/mpcs-52553-austin/tree/master/week_3/exercise_3)
