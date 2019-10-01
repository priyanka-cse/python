class CallDetail:
    def __init__(self,lis):
        self.caller=lis[0]
        self.called=lis[1]
        self.duration=lis[2]
        self.calltype=lis[3]
    def display(self):
        print(self.caller.ljust(15)+self.called.ljust(15)+self.duration.ljust(15)+self.calltype.ljust(15))
class Util:
    def __init__(self):
        self.list_of_call_objects=None
    def parse_customer(self,list_of_call_string):
        for i in list_of_call_string:
            lis=i.split(',')
            self.list_of_call_objects=CallDetail(lis)
            self.list_of_call_objects.display()
    

call1='9990000001,9330000001,23,STD'
call2='9990000001,9330000002,54,Local'
call3='9990000001,9330000003,6,ISD'
list_of_call_string=[call1,call2,call3]
print("caller".ljust(15),"called".ljust(15),"duration".ljust(15),"Type".ljust(15))
Util().parse_customer(list_of_call_string)
