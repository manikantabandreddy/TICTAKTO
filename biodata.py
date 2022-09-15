f_name = input("enter the first name : ")[:20]
l_name = input("enter the last name : ")[:20]
d_o_b = input("enter the date of birth : ")
Email=input("enter the mail id : ")
mobile= input("enter the mobile number : ")
B_tech = input("enter the b-tech clg : ")
inter = input("enter the intermediate clg : ")
ssc = input("enter the ssc : ")
skills = input("enter your skills : ")
hobbies = input("enter the hobbies : ")
address = input("enter the address : ")

if len(f_name)<=20:
    print("not more than 20 characters")
elif len(l_name)<=20:
    print("not more than 20 cgharacters")
else:
    print("not a character")
    

    

a_str1="FIRST NAME".ljust(14)
b_str2="LAST NAME".ljust(14)
c_str3="DATE OF BIRTH".ljust(14)
d_str4="EMAIL ID".ljust(14)
e_str5="MOBILE N0".ljust(14)
f_str6="B-TECH".ljust(14)
g_str7="INTERMEDIATE".ljust(14)
h_str8="SSC".ljust(14)
i_str9="SKILLS".ljust(14)
j_str10="HOBBIES".ljust(14)
k_str11="ADDRESS".ljust(14)

print("BIO DATA")
print(a_str1.ljust(14),":",f_name)
print(b_str2.ljust(14),":",l_name)
print(c_str3.ljust(14),":",d_o_b)
print(d_str4.ljust(14),":",Email)
print(e_str5.ljust(14),":",mobile)
print("EDUCATION DETAILS")
print(f_str6.ljust(14),":",B_tech)
print(g_str7.ljust(14),":",inter)
print(h_str8.ljust(14),":",ssc)
print(i_str9.ljust(14),":",skills)
print(j_str10.ljust(14),":",hobbies)
print(k_str11.ljust(14),":",address)
