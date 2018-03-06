print '''STSCI 4060 HW1
Name: Xinyi Liu
NetID: xl679'''

print '***** Question 1 *****'

print '*part a*'
# define the variable story as required, following the desired format.
story='''
Once upon a time, deep in an ancient
jungle, there lived a tiger. This tiger
liked to eat fish, but the jungle had
very little fish to offer. One day, an
explorer found the tiger and discovered
it liked fish. The explorer took the
tiger back to NYC, where it could
eat as much fish as it wanted. However,
the tiger became homesick, so the
explorer brought it back to the jungle,
leaving a large supply of fish.

-- The End of the Story --

'''
# print the story's content out to see if it's correct
print story


print '*part b*'
# replace all the strings 'tigers' with the format symbol in story
story=story.replace('tiger','%s')
# replace all the strings 'fish' with the format symbol in story
story=story.replace('fish','%s')
# print story out to see if all the required changes have been made
print story
 

print '*part c*'
# create a tuple t1, which contains all the strings we want to update in story, following the correct order
t1=('tiger','tiger','fish','fish','tiger','fish','tiger','fish','tiger','fish')
# update story by performing all the desired updates with tuple t1 
story=story%t1
# print story to see if the result is correct
print story


print '*part d*'
# replace all the strings 'tigers' with the format symbol in story
story=story.replace('tiger','%s')
# replace all the strings 'fish' with the format symbol in story
story=story.replace('fish','%s')
# create a tuple t1, which contains all the strings we want to update in story, following the correct order
t1=('monkey','monkey','bananas','bananas','monkey','bananas','monkey','bananas','monkey','bananas')
# update story by performing all the desired updates with tuple t1 
story=story%t1
# print story to see if the result is correct
print story



print '***** Question 2 *****'

print '*part a*'
# replace the word "monkey" with "%(animal)s"
story=story.replace('monkey','%(animal)s')
# replace the word "bananas" with "%(food)s"
story=story.replace('bananas','%(food)s')
# replace the word "NYC" with "%(city)s ."
story=story.replace('NYC','%(city)s')
# print out the result
print story


print '*part b*'
# define the dictionary myDict to contain required pairs with keys and values
myDict={'animal':'cat','food':'mice','city':'Beijing'}
# display the dictionary
print 'The dictionary is: ', str(myDict)
# use the string format operator and apply the dictionary to the format string
print story%myDict

print '*part c*'
# update the dictionary values with the values of "fox", "rabbits", and "London" respectively
myDict['animal']='fox'
myDict['food']='rabbits'
myDict['city']='London'
# print updates myDict
print 'The dictionary is: ', str(myDict)
# display the updated story
print story%myDict




print '***** Question 3 *****'
# create vectors u and v using list
u=[10,-2,3,44]
v=[20,3,-2,11]
# calculate the dot product of u and v
uv=u[0]*v[0]+u[1]*v[1]+u[2]*v[2]+u[3]*v[3]
# show the list representatives of u and v
print 'The list representation of vector u is: ','[[10,-2,3,44]]'
print 'The list representation of vector v is: ','[[20,3,-2,11]]'
# display the dot product
print 'The dot product u*v is: ',uv





















