fp = open('./tags.txt', 'r', encoding='utf-8')


SparseMatrix = []
TagList = []
TagCount = 0


line = fp.readline()
while line:	
	# Add tag into list and expand sparse matrix
	new_line = line.split(',')
	for tag in new_line:
		if tag not in TagList:
			TagList.append(tag)
			SparseMatrix.append([])
			for j in range(TagCount):
				SparseMatrix[j].append(0)
				SparseMatrix[TagCount].append(0)
			SparseMatrix[TagCount].append(0)
			TagCount += 1

	for i in range(len(new_line)):
		#print(line[i])
		tag_s = TagList.index(new_line[i])
		SparseMatrix[tag_s][tag_s] += 1
		for j in range(i+1, len(new_line)):
			tag_t = TagList.index(new_line[j])
			SparseMatrix[tag_s][tag_t] += 1
			SparseMatrix[tag_t][tag_s] += 1
	line = fp.readline()
fp.close()

wp = open('drawdata_edge.csv', 'w', encoding='utf-8')
wp2 = open('drawdata_node.csv', 'w', encoding='utf-8')
wp.write("Source,Target,weight\n")
wp2.write("id,Label,interval\n")
i=0
for tag in TagList:
    j=0
    cnt=0
    for tag in TagList:
        if(SparseMatrix[i][j] > 5):
            cnt+=SparseMatrix[i][j]
            wp.write(TagList[i])
            wp.write(",")
            wp.write(TagList[j])
            wp.write(",")
            wp.write(str(SparseMatrix[i][j]))
            wp.write("\n")
        j=j+1
    i=i+1
    if cnt > 0:
        wp2.write(TagList[i])
        wp2.write(",")
        wp2.write(TagList[i])
        wp2.write(",")
        wp2.write(str(cnt))
        wp2.write("\n")
wp2.close()
wp.close()
# sparse matrix as readible file
wp = open('SparseMatrix.txt', 'w', encoding='utf-8')
wp.write("        ")
for tag in TagList:
	wp.write(tag)
	wp.write('  ')
wp.write('\n')
for i in range(TagCount):
	wp.write(TagList[i])
	for j in range(TagCount):
#		n = len(str(SparseMatrix[i][j]))
#		for k in range(len(TagList[j]) + 1 - n):
#			wp.write(' ')
		wp.write('  ')
		wp.write(str(SparseMatrix[i][j]))
	wp.write('\n')
wp.close()
wp = open('SparseMatrix(weight_only).csv', 'w')
for row in range(TagCount):
	for col in range(TagCount):
		wp.write(str(SparseMatrix[row][col]))
		if (col != TagCount -1):
			wp.write(',')
	if(row != TagCount):
		wp.write('\n')
wp.close()
wp = open('Tag list.txt', 'w', encoding='utf-8')
for t in range(TagCount):
	wp.write(str(t))
	wp.write(' ')
	wp.write(TagList[t])
	wp.write('\n')
