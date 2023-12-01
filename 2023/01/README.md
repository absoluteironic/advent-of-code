# Day 1

For information about this specific puzzle, please visit https://adventofcode.com/2023/day/1.

In a sting like `1abc2` and `pqr3stu8vwx` you shall find the first and the last digit.

The quickest solution I thought of for the first puzzle was to simply loop through each letter and check if it was a digit. If true, I could then simply save it to a new string and then get the first and last digit with an index.

For the second puzzle, however, my solution did not work as well. Now, the letters could also be written as letters i.e "one", "two", "three" etc.

I had to think harder than I would like to admit and tried a lot of solutions, but nothing really worked. I then turned to regex.

I am not very good with regex and always have to spend quite some time to get my patterns to work, which is why I try to avoid it 🙃. However, I didn't really see any other solution so I made my pattern and got it to work... almost.

In a situation where the string looks like this `oneeight` you want to match both `one` and `eight`, but my solution only found a match for `one`.

I researched and learned that in an other regex library (from what I was using) there's a flag called overlapped that will return overlapping results - just like I needed. After installing the [regex library](https://pypi.org/project/regex/) everything worked 🥳.