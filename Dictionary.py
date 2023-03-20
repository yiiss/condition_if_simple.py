


def main():
    #Student={'Name':"hussein alrubaye",'Age':27,'Slary':232.5};
    Student=dict(Name="Yiiss Atlas",Age=27,Slary=232.5);
    Student['Name']="Atlas Yis"
    Student["Dept"]="Software Engineer"
    print(Student,type(Student))
    del Student["Dept"]
    print(Student,type(Student))
    print(Student['Name'])
    print(Student['Age'])
    Student.clear()
    print(Student,type(Student))
    



if __name__ == '__main__':main()
