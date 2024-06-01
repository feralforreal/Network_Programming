import time
class Days:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.Previous = None
Day1 = Days("Monday")
Day2 = Days("Tuesday")
Day3 = Days("Wednesday")
Day4 = Days("Thursday")
Day5 = Days("Friday")

Day1.next = Day2
Day1.Previous = Day5
Day2.next = Day3
Day2.Previous = Day1
Day3.next = Day4
Day3.Previous = Day2
Day4.next = Day5
Day4.Previous = Day3
Day5.next = Day1
Day5.Previous = Day4

iterator = Day1
while iterator is not Day5:
    print(iterator.value)
    iterator = iterator.next
    time.sleep(3)
while iterator:
    print(iterator.value)
    iterator = iterator.Previous
    time.sleep(3)


