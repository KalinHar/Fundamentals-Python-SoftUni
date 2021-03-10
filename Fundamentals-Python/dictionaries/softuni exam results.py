line = input()
results = {}
lang = {}
while line != 'exam finished':
    line = line.split('-')
    if len(line) == 2:
        results.pop(line[0])
    else:
        if line[0] not in results:
            results[line[0]] = int(line[2])
        else:
            if int(line[2]) > results[line[0]]:
                results[line[0]] = int(line[2])
        if line[1] not in lang:
            lang[line[1]] = 0
        lang[line[1]] += 1
    line = input()
print('Results:')
results = dict(reversed(sorted(results.items())))
results = dict(reversed(sorted(results.items(), key=lambda x: x[1])))
for r in results:
    print(f'{r} | {results[r]}')
print('Submissions:')
lang = dict(reversed(sorted(lang.items())))
lang = dict(reversed(sorted(lang.items(), key=lambda x: x[1])))
for l in lang:
    print(f'{l} - {lang[l]}')
