from test_seq2seq import ChatBot

ob=ChatBot()
while True:
    x=input("Human:")
    ans= ob.test_run(x)
    print(ans)