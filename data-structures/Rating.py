class Rating:
    def __init__(self, userId=None, itemId=None, score=None, timestamp=None, line=None):
        if line is not None:
            arr = line.split('\t')
            self.userId = int(arr[0])
            self.itemId = int(arr[1])
            self.score = float(arr[2])
            if len(arr) > 3:
                self.timestamp = long(arr[3])
        else:
            self.userId = userId
            self.itemId = itemId
            self.score = score
            self.timestamp = timestamp

    def __str__(self):
        return '<' + self.userId + ',' + self.score + ',' + self.timestamp + '>'