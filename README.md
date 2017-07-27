# Human query processing

This directory contains some notes and exercises to introduce database ideas to non-technical students (e.g., high school students).
The exercises ask groups of students to manually execute a simple database query by hand; each group gets different instructions that correspond to
different execution optimizations such as columnar data layouts, indexes, multi-threading.
The [data](https://github.com/cudbg/humanqueryprocessing/blob/master/data.csv) is a hand created set of mainly female and under-represented scientists.

This is part of [Columbia Engineering’s Inside Engineering program](https://outreach.engineering.columbia.edu/content/home), which introduces computer science and database research topics to local k-12 schools.

Discussion Notes

1. Beginning: Ask what students know about computer science or data science
  * How is it used in the world?
1. For younger kids
  * What games do they like to play?  Why?
  * Which one is the best?  Most popular?  Why?
  * How would they figure it out?
  * What year had the most popular games?  
  * Make sure they know what a decade is; what an ID is; what a table is
  * What if I gave them data to answer these questions?  What would the data look like?
		* work towards a table
1. For older kids
  * Discussion centered around starting a sneaker company.   What can computer science help with?  Eventually steer towards needs to run database queries.
    * Start a sneaker company, get endorsements from cool scientists.  How do you sell the sneakers?
    * go door to door?
    * sell online?  how do people know about you?
    * advertise?  To who?  Should you give discounts? to who?
    * who's even buying the sneakers?   steph curries vs lebrons.
      * east vs west coast?  how do you know?
      * advertise curries to east coasters? maybe there's curry fans in cleveland?  
1. Counting and asking questions is important.  But how can we make it fast?  exercise below
1. Post-exercise discussion

# Exercise

Exercises for high school students to understand query processing tricks


Overview

* Provide printouts containing snapchat-like data about students snapping other students, and "likes"
* Ask students to figure out the most popular female chat recipients and how many people snap her
* Try different plans, execution strategies, and data layouts that are translated into english steps

        SELECT extract(decade from year), count(*)
        FROM people
        WHERE gender = 'female'
        GROUP BY extract(decade from year)
        ORDER BY count(*)
        LIMIT 1

* See [./scientists](./scientists/) for exercises using dataset of scientists
* See [./games](./games/) for exercises using dataset of top video games
