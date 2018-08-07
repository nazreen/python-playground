# function to generate list of multiples of number
# takes in the multiple
# returns list
import collections
import itertools

def generateMultiplesList(x, n):
  result = []
  for i in enumerate(range(n),1):
    result.append(x * i[0])
  return result

def check():
  # get user input
  user_input = input('What are the numbers? (comma separated)')
  numbers = user_input.split(',')
  lcm = None

  multiplesLists = []

  def generateNextSetOfMultiples(multiplicationRange):
    for item in numbers:
      multiplesLists.append(generateMultiplesList(int(item), multiplicationRange))
  
  i = 0

  while not lcm:
    i = i + 10
    generateNextSetOfMultiples(i)
    multiplesListsCombined = list(itertools.chain.from_iterable(multiplesLists))
    counter = collections.Counter(multiplesListsCombined)

    frequencies = counter.most_common()
    # filter those that len(numbers) times
    presentInAll = list(filter(lambda x: x[1] == len(numbers), frequencies))
    print(len(presentInAll))
    # if 0, then redo generation
    commonFactors = list(map(lambda x: x[0], presentInAll))
    # get min
    lcm = min(commonFactors)
    print(f'The LCM is {lcm}.')

check()
