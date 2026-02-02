#Given the participants
# ' score sheet for your University Sports Day, you are required to find the runner-up score.
# You are given  scores. Store them in a list and find the score of the runner-up.

# Input Format


# The first line contains . The second line contains an array   of  integers each separated by a space.

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    largest = -101  
    runner_up = -101
    
    for score in arr:
        if score > largest:
            runner_up = largest
            largest = score
        elif score > runner_up and score < largest:
            runner_up = score
            
    print(runner_up)