class Node:
    def __init__(self):
        self.next = [-1] * 26
        self.leaf = False

def add_word(word, trie):
    v = 0
    for ch in word:
        c = ord(ch) - ord('a')
        if trie[v].next[c] == -1:
            trie[v].next[c] = len(trie)
            trie.append(Node())
        v = trie[v].next[c]
    trie[v].leaf = True


MOD = 10**9 + 7
S = input().strip()
N = int(input())
trie = [Node()]
for _ in range(N):
    word = input().strip()
    add_word(word, trie)

M = len(S)
dp = [0] * (M + 1)
dp[M] = 1
for i in range(M - 1, -1, -1):
    v = 0
    for j in range(i, M):
        c = ord(S[j]) - ord('a')
        if trie[v].next[c] == -1:
            break
        v = trie[v].next[c]

        if trie[v].leaf:
            dp[i] = (dp[i] + dp[j + 1]) % MOD
print(dp[0])

