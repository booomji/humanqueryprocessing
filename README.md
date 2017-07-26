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

        SELECT extract(decade from year), count(*)
        FROM people
        WHERE gender = 'female'
        GROUP BY extract(decade from year)
        ORDER BY count(*)
        LIMIT 1

* See [instructions.html](instructions.html) for each query execution strategy
* See [fakedata/](./fakedata/) for data sheets using made-up data for students to get aquainted with the instructions.
* See [realdata/](./realdata/) for data sheets using real data from [data.csv](./data.csv)
