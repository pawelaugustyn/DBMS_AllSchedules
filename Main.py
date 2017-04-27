from Operation import Operation
from GenerateLists import GenerateLists


if __name__=="__main__":
    t1o1 = Operation.new("r1x")
    t1o2 = Operation.new("w1x")
    t1o3 = Operation.new("r1y")
    t1o4 = Operation.new("w1y")

    Transaction1 = [t1o1, t1o2, t1o3, t1o4]

    t2o1 = Operation.new("r2z")
    t2o2 = Operation.new("r2y")
    t2o3 = Operation.new("w2y")
    t2o4 = Operation.new("r2x")
    t2o5 = Operation.new("w2x")
    Transaction2 = [t2o1, t2o2, t2o3, t2o4, t2o5]

    t3o1 = Operation.new("r3y")
    t3o2 = Operation.new("r3z")
    t3o3 = Operation.new("w3y")
    t3o4 = Operation.new("w3z")
    Transaction3 = [t3o1, t3o2, t3o3, t3o4]

    gen = GenerateLists([Transaction1, Transaction2, Transaction3])
    gen.generate_lists()
    print(gen.counter())