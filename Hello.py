text=input("say hello:")
text_list=list(text)
index_list = []
def find_index(letter):
       index_list = []
       count=0
       for a in range(len(text)):
              if text_list[a]==letter:
                 count+=1
                 index_list.append(a)

       return ((index_list,count))

about_h=find_index("h")
about_e=find_index("e")
about_l=find_index("l")
about_o=find_index("o")
if  (about_h[1]>0) & (about_e[1]>0) & (about_l[1]>1) & (about_o[1]>0):
    if about_h[0][0]< about_e[0][0]< about_l[0][0]< about_o[0][0]:
        print("welcome")

    else:
        print("you have not said hello yet!")

else:
    print("you have not said hallo yet!")