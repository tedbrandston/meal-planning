# I ran roughly this interacively

for line in d:
    if line.startswith('[**') or line.startswith('**'):
            e.append(collect)
            collect = []
    collect.append(line)

for entry in e:
    if not entry:
            continue
    x = entry[0]
    x = x.split('**')
    title = x[1]
    title = re.sub(r'\W', '_', title)
    with open(f'content/{title}.md', 'w') as wfp:
            wfp.write(''.join(entry))

for f in os.listdir():
	with open(f) as rfp:
		lines = rfp.readlines()
	x = lines[0]
	x = x.split('**')
	title = x[1]
	url = ''
	if len(x) > 2:
		url = x[2]
		url = url.strip('])( \n*')
	tags = ['needs-attention']
	for i in range(len(lines)):
		if lines[i].startswith('tags:') or  lines[i].startswith('Tags:'):
			tag_line = lines[i]
			lines.remove(tag_line)
			tag_line = tag_line[5:]
			tags += tag_line.split(',')
			break
	tags = (tag.strip() for tag in tags)
	tags = ', '.join(tags) 
	lines.remove(lines[0])
	with open(f, 'w') as wfp:
		wfp.write('---\n')
		wfp.write(f'title: {title}\n')
		wfp.write(f'tags: {tags}\n')
		wfp.write(f'link: {url}\n')
		wfp.write('---\n')
		wfp.writelines(lines)

