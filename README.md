# Implementation

### Data Structures

I used two data structures for this assignment: 

+ dictionary
+ binary heap  

I created two tables and one heap:   

+ a patients table that stored drug and patient information  
+ a drugs table that stored a drugs, accumulated costs, and number of unique counts
+ a heap to store keep track of accumulated costs, drugs, and number of unique counts

I chose a dictionary for the patients table so that I could access and set information in the table in $O(1)$ time.  Likewise, I chose a drugs table for the same reasons.  I chose a binary heap since to heapify the drugs table it costs $O(n\log(n))$ and to pop off the top to print it's $O(n)$.  My efficiency should be of the order $O(n\log(n))$. 

### Code Description

I have two functions main() and pharm_count() and everything else are classes with member functions. I modularized the code and ran several small and long cases.  I profiled my code to see whether I could improve some of the layout.  I ran unit tests.  
