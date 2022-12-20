def same_by(characteristic, objects):
    result = list(map(characteristic, objects))
    print(all([i == result[0] for i in result]))
same_by(lambda x: x % 2, [2,4,6,8])
same_by(lambda x: x % 2, [2,4,7,8])