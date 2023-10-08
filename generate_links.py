file = open('ids.txt', 'r')
ids = file.read().splitlines()
file.close()
file = open('xhs.txt', 'w')
for id in ids:
  file.write('https://www.xiaohongshu.com/explore/' + id + '\n')
file.close()
