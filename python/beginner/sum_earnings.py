#Code to sum all earnings
def sum_earnings(input):
  try:
    money=list(map(int, input.split(',')))
  except:
    return 0

  total_money=reduce((lambda x, y : x+y), money)
  if total_money<0:
    total_money=0
  return total_money