'''
Question 4
the variables are preceeded by the keyword global so that the varaiables can be called apon the rest of the program

Question 10
The three functions are:
1. to get the names from the learderboard file
2. to get the scores from the leaderboard file 
3. updates the leaderboard if there is a new high score

Question 11
When I ran my code, I was able to enter my username in the terninal. After that, the game ran fine for me.
When I checked the terminal after the game was over, I got an error. It said that there was no such file or directory
of a112_leaderboard.txt

Question 12
The function opens the file that we have selected in read mode

Question 13
The first line of code creates the list
The second line of code creates a variable equal to the 3rd item in the list
The third line of code prints out the variable created

Question 14
part a. It printed mouse, which is the thrid item in the list
part b. if you want the code to print monkey, then you have to change: animal = animals_list[4]

Question 15 
it will insert horse in between at and mouse. Then it will print out that list.

Question 16
part a. I was wrong in my answer to question 15. It actually replaces mouse, and mouse is not there anymore
part b. to change dog into wolf you have to do: animals_list[0] = "wolf"

Question 17
there is not enough elements in the list when you are reffering to index 5

Question 18
part a.
The first line sets the leader name to a null value
The second line sets the idex to zero
The third line is a while loop that compairs a single sting to ,
The forth line is to change the leader name the sting plus the previous string if it passed line three.
The firth line adds 1 to the index.
part b.
the loop ends when the index reaches a comma

Question 19
part b. we can use a print statement to print out the values that we are working with
part c. The line of code should be outside the loop so that we can get the final name, not just each letter increments.
part e. my code worked as expected

Question 23
The boolean expression should check if it is a new line

Question 30
x = "asdfghj"
print(len(x))
The value of index is at 5, and it is the same as the lenght of the list

Question 31
the lion was inserted at index 4, without replacing a element

Question 33
Cat was popped

Question 34
it removed dog, and the list stayed that way when it was called again

Question 41
For loops work by going until the condition is met. A break is useful so that the code can continue to the next segment of code

Question 44
The write function puts the data back into the learderboard.txt file

Question 47
part a. The if statement checks if the player has made the learderboard yet
part b. The boolean is used to check if the player made the leaderboard and is used to display the message

Question 50
the results will be false, true, true, false

Conclusion
1. - you can excess a chacater in a string or an element in a list by iterating through them
   - A string can only hold string data types, while a list can hold a mixture of any type of data type. 
   - you can use a lot of different methods to strings and list. They usually add, delete, or insert more values

2. - when you call a list, that is abstraction
   - using methods that manipulate variables over and over again, like in a loop
   - when we picked which scores should be in the leaderboard by going thorugh the index

3. I used a for loop when going though the index of the leader names. 
   It made sense because I want it to go though each of the elements in leader names
    for index in range(len(leader_names)):
        leaderboard_file.write(leader_names[index] + "," + str(leader_scores[index]) + "\n")
   
   I used a while loop going though the index until it ran into a comma. 
   It made sense to use it because I didnt know where the comma was, and so it kept going until it found it.
    while (line[index] != ","):
      leader_name = leader_name + line[index] 
      index = index + 1
'''