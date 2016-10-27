def get_max_topi_team_count(topic):
    max_count = 0
    team_count = 0
    for i in range(len(topic)):
        for j in range(i + 1, len(topic)):
            val = int(topic[i], 2) | int(topic[j], 2)
            topic_count = bin(val).count('1')
            if topic_count == max_count:
                max_count = topic_count
                team_count += 1
            elif topic_count > max_count:
                max_count = topic_count
                team_count = 1
    return max_count, team_count


if __name__ == '__main__':
    n, m = raw_input().strip().split(' ')
    n, m = [int(n), int(m)]
    topic = []
    for _ in xrange(n):
        topic.append(raw_input().strip())
    max_count, team_count = get_max_topi_team_count(topic)
    print max_count
    print team_count
