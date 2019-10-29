#Draius Disimone Lab 8
#Heating Cooling Lab 

def main():
        temp= input("Input the average # of tempurature a day separated by commas: ")
        temp=temp.split(", ")
        heatdays=0
        cooldays=0

        for i in temp:
            if float(i) > 80 or float(i) < 60:
                if float(i)> 80:
                    cooling += float(i)-80
                else:
                    heating += 60 - float(i)

        print("There is", cooldays, "cool degree days and ", heatdays, "heat degree days")
main()
