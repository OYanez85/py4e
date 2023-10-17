# a combination of a loop with a exit mechanism. We have some sanity checking of
# our input, so making sure that we have some valid input and we catch it and
# we use continue to loop back up to run the next iteration of the loop. We
# have an accumulator pattern and then we can use the accumulated data to print
# what we want to print
num = 0
tot = 0.0
while True :
  sval = input('Enter a number:')
  if sval == 'done':
      break
  try:
      fval = float(sval)
  except:
      print('Invalid input')
      continue
  # print(fval)
  num = num + 1
  tot = tot + fval

# print('ALL DONE')
print(tot,num,tot/num)
