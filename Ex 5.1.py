class nisit:
    def __init__(self,name,clss,subject,sex,province):
        self.name = name
        self.sex = sex 
        self.clss = clss 
        self.subject = subject 
        self.province = province
    def introdue(self):
        print("-"*40,"แนะนำตัว"+"-"*40)
        if self.sex == "ชาย":
            print("สวัสดีครับผมชื่อ : ",self.name +" นักศึกษาชั้นปีที่ : ",self.clss +" สาขาวิชา : ",self.subject +" เพศ : ",self.sex +" มาจากจังหวัด : ",self.province)
        else :
            print("สวัสดีค่ะดิฉันชื่อ : ",self.name +" นักศึกษาชั้นปีที่ : ",self.clss +" สาขาวิชา : ",self.subject +" เพศ : ",self.sex +" มาจากจังหวัด : ",self.province)
data = []
a = input("ชื่อ-สกุล : ชั้นปี : สาขา : เพศ : จังหวัด : ")
split_a = a.split(":")
data.append(split_a[0])
data.append(split_a[1])
data.append(split_a[2])
data.append(split_a[3])
data.append(split_a[4])
x = nisit(data[0],data[1],data[2],data[3],data[4])
x.introdue()
