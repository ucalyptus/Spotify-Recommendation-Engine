from io import BufferedReader
import random
class SortMapExample:
	def main(self,args):
		self.tmap = {
			1:2.0,
			1:3.0,
			1:1.0,
			3:2.0,
			4:0.0
		}
		print(self.tmap)

class StopwordsFilter:
	isInitialized=False
	def init(self,stopwordsFile):
		if !isInitialized:
			reader=BufferedReader
		while line = reader.readLine is not None:
			stopword=line.trim().lower()
			self.stopwords.insert(stopword)
			stopword=stopword.replaceAll("[^\\w]","")
			self.stopwords.insert(stopword)
		self.stopwords.insert('\t')
		reader.close()
		isInitialized=True

	def isStopword(self,word):
		return (word.lower() in self.stopwords)

	def main(self,args):
		StopwordsFilter.init('lib/stopwords.txt')
		print(isStopword('the'))


class Printer:
	def printArray(self,A):
		print(A)

	def printTime(self,msType):
		original=msType
		ms=msType%1000
		original=original//1000
		sec=original%60
		original//=60
		minute=original%60
		original=original//60
		hr=original%60
		original=original//24
		day=original
		if day > 1:
			return f"{day} days, {hr}:{minute}:{sec}:{ms}"
		elif day > 0:
			return f"{day} day, {hr}:{minute}:{sec}:{ms}"
		else:
			return f"{hr}:{minute}:{sec}:{ms}"

class CommonUtils:
	def ShuffleArray(self,array):
		i=len(array)-1
		while i>0:
			index=random.random(0,i+1)
			temp=array[index]
			array[index]=array[i]
			array[i]=temp

	def StringToGramSet(self,str,k):
		words=str.split(" ")
		grams=[]
		for i in range(len(words)+1):
			gram=words[i]
			for j in range(1,k):
				gram+=" "+words[i+j]
			grams.append(gram.trim())
		return grams

	def CountMatchesInString(self,str,findStr):
		return str.count(findStr)

	def ArrayToArraylist(self,array):
		if array is None:
			return []
		else:
			return list(array)

	def TopKeysByValue(self,map,topK,ignoreKeys):
		ignoreSet=()
		if ignoreSet is None:
			ignoreSet=()
		else:
			ignoreSet=()*ignoreKeys

		topQueue = TopKPriorityQueue(topK)

		for entry in map:
			if entry is not in ignoreSet:
				topQueue.add(entry,map[entry])

		topKeys=[]
		for entry in topQueue.sortedList():
			topKeys.append(entry)

		return topKeys

	def SortMapByValue(self,map):
		inFolds=list(map)
		def compare(o1,o2):
			return map[o2].-map[o1]
		sort(inFolds,cmp=compare)
		return inFolds

class TopKPriorityQueue():
	def compare(o1,o2):
		return o1.values()-o2.values()

	def __init__(self,maxSize):
		if maxSize<=0:
			raise IllegalArgumentException()
		self.K=maxSize
		self.queue=[]

	def add(self,e):
		if len(self.queue<self.K):
			self.queue.append(e)
		else:
			peek = queue[0]
			if compare(e,peek)>0:
				queue.pop(peek)
				queue.append(e)

	def sortedList(self):
		list_=self.queue
		sort(list_,cmp=compare,reverse=True)
		return list_

	def toList(self):
		return list(self.queue)

	def maxPoolingIndices(self,vec,maxPooling):
		indexList=[]
		q=TopKPriorityQueue(maxPooling)
		for i in range(vec.size()):
			q.add(i,vec.get(i))
		for e in q:
			indexList.append(e,q[e])
		return indexList

	def main(self,args):
		q=TopKPriorityQueue(3)
		map_={1:1.0,2:2.0,3:4.0,4:3.0}
		for e in map_:
			q.add(e,map_[e])

		q.add(6,5.0)
		q1=q.sortedList()
		for e in q1:
			print(str(e)+": "+q[e])

		array=[3,1,5,6,2]
		Printer.printArray(array)
		for i in array:
			print(i,end=" ")