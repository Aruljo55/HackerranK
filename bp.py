def isWinning(n, config):
    from functools import lru_cache

    @lru_cache(None)
    def grundy(length):
        if length < 3:
            return 0
        grundy_set = set()
        for i in range(length - 2):
            # simulate removing 3 pieces starting from i
            left = grundy(i)
            right = grundy(length - i - 3)
            grundy_set.add(left ^ right)
        # mex (minimum excluded value)
        g = 0
        while g in grundy_set:
            g += 1
        return g

    segments = []
    count = 0
    for ch in config:
        if ch == 'I':
            count += 1
        else:
            if count > 0:
                segments.append(count)
                count = 0
    if count > 0:
        segments.append(count)

    xor_sum = 0
    for seg in segments:
        xor_sum ^= grundy(seg)

    return "WIN" if xor_sum != 0 else "LOSE"
