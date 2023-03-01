#Name: Sophia Philips
#GitHub Username: sophiacphilips
#Date: 03/01/2023
#This code is designed to create a sequence like this using a generator function: 2, 12, 1112, 3112, 132112, 1113122112, 311311222112, 13211321322112...
#"To get a term of the sequence, count how many there are of each digit (in a row) in the previous term. For example, the
#first term is "one 2", which gives us the second term "12". That term is "one 1" followed by "one 2", which gives us
# the third term "1112". That term is "three 1" followed by "one 2", or 3112. Etc." (from instructions)




def count_seq():
    #count sequence generator function
    val = "2"
    #starting variable for counting sequence (special case)

    while True:

        yield val

        string,count = val[0],0
        if len(val)==1:

            val = "12" #special case to start sequence

        else:
            next_val= ""

            for num in val:
                if num == string:
                    count+=1
                else:
                    next_val = next_val + str(count) + string
                    string = num
                    count = 1
            next_val = next_val + str(count) + string
            val = next_val

cq = count_seq()
