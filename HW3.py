from functools import reduce
import sys

# When debug is false, no traceback will be printed in the code.
# When it is true, traceback will be printed. 
debug = False
if(debug):
    # Default tracebacklimit value.
    sys.tracebacklimit = 1000
else:
    sys.tracebacklimit = 0

# sprintLog takes a sprint and returns a list of each task with the amount of hours each dev worked on it logged.
def sprintLog(sprnt):
    # List of tasks
    tasks = {}
    # For each dev and their tasks in the sprint:
    for dev, tasks_completed in sprnt.items():
        # For each task and it's respective hours in the sprint:
        for task, hours in tasks_completed.items():
            # If the task exists, add the hours to the existing value for that dev, or add a new entry with the hours
            # for that dev.
            if task in tasks:
                if dev in task:
                    tasks[task][dev] += hours
                else:
                    tasks[task][dev] = hours
            # Otherwise, create a new task with the dev's name and hours.
            else:
                tasks[task] = {dev: hours}
    # Return the list of tasks.
    return tasks

# Add sprint has the same functionality as sprintLog, but repeats it for the parameterized sprints and merges
# them into a single list.
def addSprints(sprint1, sprint2):
    # Merged list
    merged_tasks = {}
    
    # For first sprint:
    for task, dev in sprint1.items():
        # For each task, if it is in the merged list:
        if task in merged_tasks:
            # For each dev and each dev's hours in the task's list:
            for dev, hours in dev.items():
                # Get the hours already logged, and then add the hours from the first sprint.
                merged_tasks[task][dev] = merged_tasks[task].get(dev, 0) + hours
        # If the task is not in the first list:
        else:
            # Create a new entry in the merged dictionary
            merged_tasks[task] = {}
            # Now, for each dev and their hours, add it to the new entry.
            for dev, hours in dev.items():
                merged_tasks[task][dev] = hours
    
    # For second sprint:
    for task, dev in sprint2.items():
        # For each task, if it is in the merged list:
        if task in merged_tasks:
            # For each dev and each dev's hours in the task's list:
            for dev, hours in dev.items():
                # Get the hours already logged, then add the hours from the first sprint.
                merged_tasks[task][dev] = merged_tasks[task].get(dev, 0) + hours
        # If the task is not in the first list:
        else:
            # Create a new entry in the merged dictionary
            merged_tasks[task] = {}
            # Now, for each dev and their hours, add it to the new entry.
            for dev, hours in dev.items():
                merged_tasks[task][dev] = hours
    
    # Return the merged task list.
    return merged_tasks

# addNLogs uses sprintLog and addSprints to create a list from n amounts of logs, defined as logList.
def addNLogs(logList):
    # Using map, we can create a map object holding all of the sprints as dictionaries.
    sprints = map(sprintLog, logList)
    
    # Using reduce, we can apply addSprints to each object and the one after it cumulatively,
    # sort of collapsing each next sprint dictionary into the total dictionary.
    merged_sprint = reduce(addSprints, sprints)
        
    # Return the full, single dictionary of all of the sprints.
    return merged_sprint

def lookupVal(L, k):
    # For each dictionary, starting from the end,
    for dictionary in reversed(L):
        # If k exists in the dictionary, then return the value.
        # By returning the value immediately, it will always return the first one.
        if k in dictionary:
            return dictionary[k]
    # return none if not found.
    return None

def lookupVal2(tL, k):
    
    # Get the first index, aka the last tuple
    first_index = len(tL) - 1
        
    # Recursive function
    def lookupValHelper(tL, k, next_index):
        
        # Get current index and dictionary from the previous recursive call
        index, dictionary = tL[next_index]
        # If k exists, return the value immediately.
        if k in dictionary:
            return dictionary[k]
    
        # If the index is 0 and the next index is also 0, we have reached the end, so we return none.
        if index == 0 and next_index == 0:
            return None
        # Otherwise, move to the next index defined by the first value in the current index's tuple.
        else:
            next_next_index = index
            return lookupValHelper(tL, k, next_next_index)

    # Recursive Call
    return lookupValHelper(tL, k, first_index)


def unzip(L):
    # By unpacking the list, and then calling zip, we unpack each element and then combine them back into transposed lists
    # of the elements in each list, aka the first elements from each tuple are a list, second are a list, and so on.
    # Then, we just return a tuple filled with these elements.
    return tuple(zip(*L))

# Finds the amount of paths a robot can take to get to the bottom corner. By recursively calling many times with increasing
# values, we can find all of the paths which are not blocked and add them together.
def numPaths(m, n, blocks):

    # Recursive helper function
    def numPathsHelper(x, y):
        # If the path is found, return 1 (aka add 1 to the amount of paths).
        if x == m and y == n:
            return 1
        
        # If our next move, right or down, is blocked, we can return 0 (no path available).
        if (x,y) in blocks:
            return 0
        
        # Variable to store the amount of rightward paths found.
        rightwards = 0
        # As long as x is smaller than m, we recursively call while increasing the rightwards value.
        if x < m:
            rightwards = numPathsHelper(x + 1,y)
        
        # Variable to store the amount of downward paths found
        downwards = 0
        # As long as y is smaller than n, we recursively call while increasing the downwards value.
        if y < n:
            downwards = numPathsHelper(x, y + 1)
        
        # We add the values together to find the total paths.
        return rightwards + downwards
    
    # Return the paths starting from (1,1) aka top left corner.
    return numPathsHelper(1,1)

# iterFile defines an iterator which reads a file word by word and returns the next word only when __next__() is called.
# iterFile uses a generator to cleanly get the next word without reading line by line or the entire file.
# iterFile raises a StopIteration error when the end of the file is reached.
class iterFile:
    # Initialize iterator.
    def __init__(self, filename):
        # Try and catch FileNotFound, and tell user that the file was not found.
        try:
            self.file = open(filename, "r")
        except FileNotFoundError:
            print("File not found.")
        self.words_generator = self.generate_words()

    # Define iterator. For this one, I do not have the iterator itself do anything specific, only __next__.
    def __iter__(self):
        return self

    # When __next__ is called, return the next word.
    def __next__(self):
        # Try to return the next word
        try:
            return next(self.words_generator)
        # If there is no next word, print message and raise the error again to end the iterator.
        except StopIteration:
            print("End of file or file is empty.")
            self.file.close()
            raise

    # Generator which gets the next word in the file provided there is another word.
    # Essentially, it reads through each line and then each word, strips it, and yields it.
    # This is a clean and easy way to get the next word without storing the line, and generators
    # automatically throw StopIteration errors which was caught in __next__().
    def generate_words(self):
        for line in self.file:
            for word in line.split():
                if word.strip == "":
                    yield None
                yield word.strip()

# wordHistogram just reads through the parameterized words and creates a histogram of their frequencies.
def wordHistogram(words):
    word_histogram = {}
    # For each word, create an entry with the value 0 or add 1 to the existing value.
    for word in words:
        word_histogram[word] = word_histogram.get(word, 0) + 1
    # Return the histogram as a tuple.
    return tuple(word_histogram.items())
