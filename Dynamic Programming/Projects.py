def max_money(N, projects):
    times = []
    for idx, (start, end, reward) in enumerate(projects, start=1):
        times.append((start, idx, 0))  # 0 for start
        times.append((end, idx, 1))    # 1 for end

    times.sort()

    mp = {}
    for idx, (time, _, _) in enumerate(times, start=2):
        if time not in mp:
            mp[time] = idx

    dp = [0] * (2 * N + 2)
    for i in range(2, 2 * N + 2):
        time, proj_id, typ = times[i - 2]
        if typ == 0:  # Start of a project
            dp[i] = dp[i - 1]
        else:  # End of a project
            start_time, _, reward = projects[proj_id - 1]
            dp[i] = max(dp[i - 1], dp[mp[start_time] - 1] + reward)

    return dp[2 * N + 1]

# Accepting input from the user
N = int(input())
projects = [tuple(map(int, input().split())) for _ in range(N)]

# Finding the maximum amount of money
result = max_money(N, projects)
print(result)

