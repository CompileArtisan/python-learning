import re
def main():
    # Search for pattern 'iii' in string 'piiig'.
    # All of the pattern must match, but it may appear anywhere.
    # On success, match.group() is matched text.
    match = re.search(r'iii', 'piiig')
    if match:
        print(match)
        print(match.group())
    else:
        print('Not found')
        
    print('-------------------')
        
    # . = any char but \n
    match = re.search(r'..g', 'piiig')
    if match:
        print(match)
        print(match.group())
    else:
        print('Not found')
        
    print('-------------------')
    
    # \d = digit char, \w = word char
    match = re.search(r'\d\d\d', 'p123g')
    if match:
        print(match)
        print(match.group())
    else:
        print('Not found')
        
    print('-------------------')
    
    match = re.search(r'\w', 'adi athadi')
    if match:
        print(match)
        print(match.group())
    else:
        print('Not found')
        
    print('-------------------')
    
    # i+ = one or more i's, as many as possible.
    match = re.search(r'pi+', 'piiig')
    if match:
        print(match)
        print(match.group())
    else:
        print('Not found')
        
    print('-------------------')
    
    # Finds the first/leftmost solution, and within it drives the +
    # as far as possible (aka 'leftmost and largest').
    # In this example, note that it does not get to the second set of i's.
    match = re.search(r'i+', 'piigiiii')
    if match:
        print(match)
        print(match.group())
    else:
        print('Not found')
        
    print('-------------------')
    
    # \s* = zero or more whitespace chars
    # Here look for 3 digits, possibly separated by whitespace.
    match = re.search(r'\d\s*\d\s*\d', 'xx1 2   3xx')
    if match:
        print(match)
        print(match.group())
    else:
        print('Not found')
        
        
    print('-------------------')

    # ^ = matches the start of string, so this fails:
    match = re.search(r'^b\w+', 'foobar')
    if match:
        print(match)
        print(match.group())
    else:
        print('Not found')
        
    print('-------------------')
    
    # But without the ^ it succeeds:
    match = re.search(r'b\w+', 'foobar')
    if match:
        print(match)
        print(match.group())
    else:
        print('Not found')
        
    print('-------------------')
    
    # match email address
    str = 'purple'
    match = re.search(r'^\w+', str)
    if match:
        print(match)
        print(match.group())
    else:
        print('Not found')
        
    print('-------------------')
    
    # match email address
    str = 'purple@example.com'
    match = re.search(r'\w+@\w+\.\w+', str)
    if match:
        print(match)
        print(match.group())
    else:
        print('Not found')
        
    print('-------------------')
    
    # replace a word
    str = 'the quick brown fox'
    match = re.sub(r'fox', 'bear', str)
    print(match)
    
    print('-------------------')
    
    # functions you can do with regex:
    # re.match()
    # re.sub()
    # re.findall()
    # re.split()
    # re.search()
    
    # explanation of these functions:
    # re.match() - checks for a match only at the beginning of the string.
    # re.search() - checks for a match anywhere in the string.
    # re.findall() - returns a list of all matches.
    # re.split() - returns a list of all matches.
    # re.sub() - replaces one or many matches with a string.
    
    # re.match() and re.search() return None if no match is found.
    # If a match is found, a match object instance is returned.
    # This object instance contains information about the match.
    # The group() method returns the part of the string where there was a match.
    # The start() and end() methods return the start and end positions of the first match.
    # The span() method returns a tuple containing the (start, end) positions of the match.
    # The string attribute returns the string passed into the function.
    # The re.sub() function replaces the matches with a string.
    # The re.sub() function returns a new string.
    # The re.sub() function takes the following parameters:
    # The pattern to search for.
    # The replacement string.
    # The string to search.
    # The number of replacements to make.
    # The re.findall() function returns a list of all matches.
    # The re.findall() function takes the following parameters:
    # The pattern to search for.
    # The string to search.
    # The re.split() function returns a list of all matches.
    # The re.split() function takes the following parameters:

    # The pattern to search for.
    # The string to search.
    # The maximum number of splits to make.
    # The re.split() function returns a list of all matches.
    # The re.split() function takes the following parameters:
    # The pattern to search for.
    # The string to search.
    # The maximum number of splits to make.
    
if __name__ == "__main__":
    main()