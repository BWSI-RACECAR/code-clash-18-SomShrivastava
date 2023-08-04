"""
Copyright MIT BWSI Autonomous RACECAR Course
MIT License
Summer 2023

Code Clash #18 - Talking Clock (talkingclock.py)


Author: Andrew Scott White

Difficulty Level: 8/10

Prompt: I don’t want to be late for the BWSI Grand Prix, so I want
to program my phone to update me on the time. Can you help me make 
a Talking Clock? I need a script that takes an input 24-hour time 
(00:00 - 23:59) and translates it into words. Please format the input 
as ‘##:##’ and include am/pm in the output string. Thanks!

Test Cases:
Input: 12:00  Output: It's twelve pm

Input: 23:59  Output: It's eleven fifty nine pm

Input: 12:05  Output: It's twelve oh five pm
"""

first_number = {
    "01": "one",
    "02": "two",
    "03": "three",
    "04": "four",
    "05": "five",
    "06": "six",
    "07": "seven",
    "08": "eight",
    "09": "nine",
    "10": "ten",
    "11": "eleven",
    "12": "twelve"
}

second_number = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
    "10": "ten",
    "11": "eleven",
    "12": "twelve",
    "13": "thirteen",
    "14": "fourteen",
    "15": "fifteen",
    "16": "sixteen",
    "17": "seventeen",
    "18": "eighteen",
    "19": "nineteen"
}

second_second_number = {
    "1": "ten",
    "2": "twenty",
    "3": "thirty",
    "4": "forty",
    "5": "fifty",
    "6": "sixty",
    "7": "seventy",
    "8": "eighty",
    "9": "ninety",
}

    # This will convert military hours to regular hours, and determine AM vs PM
class Solution:    
    def ClockTalker(self, input_time):
            #type input_time: string
            #return type: string
            
            end = "pm" if int(input_time.split(":")[0]) >= 12 else "pm"
            print(end)
            
            if input_time == "00:00":
                return "It's twelve am"
            
            first = input_time.split(":")[0]
            if first == "00":
                first = "12"
            first = str(int(first) - 12 if int(first) > 12 else int(first))
            second = input_time.split(":")[1]
            
            oh = False
            second_word = ""
            
            if second == "00":
                second_word = ""
            else:
                if int(second) < 10:
                    oh = True
                if int(second) <= 19:
                    if int(second) < 10:
                        second_word = first_number[second] + " "
                    else:
                        second_word = second_number[second] + " "
                else:
                    second_word = second_second_number[second[0]] + " " + second_number[second[1]] + " "
                            
            return "It's " +  second_number[first] + (" oh " if oh else " ") + second_word + end
            #TODO: Write code below to return a string with the solution to the prompt.

def main():
     str1=input()
     tc1= Solution()
     ans=tc1.ClockTalker(str1)
     print(ans)
    
if __name__ == '__main__': 
    main()
