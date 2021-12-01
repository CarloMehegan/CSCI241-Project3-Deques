from Hanoi import Hanoi

#use the following as the main method for the actual Hanoi file

# if __name__ == "__main__":
#   # n=12
#   # runtime = timeit.timeit("Hanoi(n)", setup="from __main__ import Hanoi,n", number=1)
#   # print("computed Hanoi(" + str(n) + ") in " + str(runtime) + " seconds.")

#   times = dict()
#   for n in range(1,13):
#     total = 0
#     for _ in range(100):
#         runtime = timeit.timeit("Hanoi(n)", setup="from __main__ import Hanoi,n", number=1)
#         total += (runtime*100000) #microseconds
#     times[n] = (total / 100)
#     print("ran Hanoi(" + str(n) + ") ten times")

#   print("success. averages:")
#   print(str(times))