from sys import argv
script,case_number,case_name,assertion=argv
file_name='case002.txt'
print("用例编号:",case_number)
print("用例名称",case_name)
print("断言",assertion)
target=open(file_name,'w')
print("truncating the file.goodbye!")
print("write file:",file_name)
target.write("用例编号:",)
target.write("\n")
target.write("用例名称:",)
target.write("\n")
target.write("断言",)
target.write("\n")
target.close()