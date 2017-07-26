# Human query processing

1. Ask what students know about computer science or data science
  * How is it used in the world?
  * Give some examples. Start a sneaker company, get endorsements from cool scientists.  How do you sell the sneakers?
    * go door to door?
    * sell online?  how do people know about you?
    * advertise?  To who?  Should you give discounts? to who?
    * who's even buying the sneakers?   steph curries vs lebrons.
      * east vs west coast?  how do you know?
      * advertise curries to east coasters?
      * maybe there's curry fans in cleveland?  
2. How do you make it fast?  exercise

# Exercise

Exercises for high school students to understand query processing tricks


Overview

* Provide printouts containing snapchat-like data about students snapping other students, and "likes"
* Ask students to figure out the most popular female chat recipients and how many people snap her
* Try different plans, execution strategies, and data layouts that are translated into english steps

        SELECT name, count(*)
        FROM chats
        WHERE gender = Female
        GROUP BY name
        ORDER BY count DESC
        LIMIT 1

* Each team has a minute to strategize how to run the algorithms

        Single thread, row oriented

        1. filter by gender = Female
        2. figure out the distinct names
        3. for each name
          4. count
        5. sort by count desc
        6. pick the first


        Single thread, row oriented, better

        1. filter by gender = Female
        3. build hash table of name, count
        4. read through the counts and remember the biggest one


        5-threads, row oriented, better

        0. give each student 1/5 of the pages
        1. run single threaded, row oriented


        10-threads, row oriented, thread contention

        0. give each student 1/5 of the pages
        1. run single threaded, row oriented


        Col oriented

        0. print page for each column
        1. filter by gender = Female
        2. build hash table of name, count
        3. pick biggest one

        Col oriented, partition by gender

        0. print page for each column
        1. filter by gender = Female
        2. build hash table of name, count
        3. pick biggest one

 
        Indexed by name --> chats

        1. filter by gender = Female
        2. for each name, lookup in index and count number of entries
        3. keep track of biggest count

* See data in data.csv

        SELECT extract(decade from year), count(*)
        FROM people
        WHERE gender = 'female'
        GROUP BY extract(decade from year)
        ORDER BY count(*)
        LIMIT 1
