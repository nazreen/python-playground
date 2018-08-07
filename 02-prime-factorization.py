def check() :
  user_input = int(input('What is the number?\n'))

  def join_l(l, sep):
      li = iter(l)
      string = str(next(li))
      for i in li:
          string += str(sep) + str(i)
      return string

  def prime_factors(n):
      i = 2
      factors = []
      while i * i <= n:
          if n % i:
              i += 1
          else:
              n //= i
              factors.append(i)
      if n > 1:
          factors.append(n)
      return join_l(factors, ' ')

  print(prime_factors(user_input))
  check()

check()