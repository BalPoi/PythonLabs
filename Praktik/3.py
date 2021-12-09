S = input().split()
for i in range(0, len(S)):
    if not S[i].isupper():
        S[i] = S[i].capitalize()

print(" ".join(S))
