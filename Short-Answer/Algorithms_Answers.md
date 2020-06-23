#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) O(n): the while loop won't stop until a >= n^3. The increment of a every time is n^2. n^3 / n^2 = n. It takes nth time to run the loop regardless the n value.

b) O(n log n): for loop will run nth times and the nested while loop will run n/2 times. When exit the while loop, j value would be over written. For the worst case scenario, it would be n+n/2. So it would be O(n log n)

c) O(n): the is linear. This function will be called "bunnies" time before reach base case.

## Exercise II

1. Understand
   nth floor
   plenty of eggs
   drop an egg equal or higher than f floor, egg gets broken
   otherwise egg is safe

   Goal: find out the value of f when the number of dropped + broken eggs is minimized.

2. Plan
   Given the problem, we know that an egg will break when dropped at f floor. To find this f, a binary search will help.

3. Execute
   floors = n

   looping through the floors, we start by dropping the egg at n/2 floor: start_floor = n/2
   if egg breaks, (we need to go to the lower half floors to do the same)
   then reassign the value of start floor = start_floor/2
   else (we need to go to the higher half floors to do the same)
   then reassign the value of start floor = start_floor + start_floor/2
   We loop through until there are only there are 2 floors left.  
   If the current_floor = j and the egg breaks
   then f = j -1
   If it does not break,
   then f = j

4. Reflect
   This is O(log n) since we use binary search
