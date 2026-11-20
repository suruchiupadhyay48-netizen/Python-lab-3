#------------------ loops and while -----------------#

#Task 1: Simulate Bookings Using While Loop

#In the Railway Reservation System, passengers continuously request ticket bookings until all seats are occupied.

#While Loop : A while loop is used to repeatedly execute a block of code as long as a condition is true.

#A while loop is used because the booking process continues until the available seats become zero.

total_seats = 5

while total_seats  > 0:
  print("Seat Booked Successfully")
  print("Remaining Seats :", total_seats -1)
  total_seats -=1
print("All seats are failles")