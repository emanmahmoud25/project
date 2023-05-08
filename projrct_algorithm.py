def job_scheduling(jobs):
    jobs.sort(key=lambda x: x[2], reverse=True) # sort jobs in decreasing order of their profits
    n = len(jobs)
    slots = [False] * n
    profit = 0
    count = 0
    for i in range(n):
        for j in range(min(n, jobs[i][1])-1, -1, -1): # find the latest available slot for the job
            if not slots[j]:
                slots[j] = True
                profit += jobs[i][2]
                count += 1
                break
    return (count, profit)
jobs = [(1,4,20),(2,1,10),(3,1,40),(4,1,30)]
print(job_scheduling(jobs))

def max_profit(jobs):
    # Step 1: Sort jobs by end time
    jobs.sort(key=lambda x: x[1])
    
    # Step 2: Initialize DP array
    n = len(jobs)
    dp = [0] * (n+1)
    
    # Step 3: DP algorithm to compute maximum profit
    for i in range(1, n+1):
        j = i - 1
        while j >= 0 and jobs[j][1] > jobs[i-1][0]:
            j -= 1
        dp[i] = max(dp[i-1], dp[j+1] + jobs[i-1][2])
    
    # Step 4: Compute solution by backtracking through DP array
    solution = []
    i = n
    while i > 0:
        if dp[i] != dp[i-1]:
            solution.append(jobs[i-1])
            j = i - 1
            while j >= 0 and jobs[j][1] > jobs[i-1][0]:
                j -= 1
            i = j + 1
        else:
            i -= 1
    solution.reverse()
    
    # Step 5: Return maximum profit and solution as tuple
    return dp[n], solution

# Example input
Jobs = [[1, 6, 6], [2, 5, 5], [5, 7, 5], [6, 8, 3]]

# Compute solution and print output
max_profit, solution = max_profit(Jobs)
print("Maximum profit:", max_profit)
print("Solution:", solution)
