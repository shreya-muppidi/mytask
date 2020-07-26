import csv
def write_into_csv(info_list):
  with open('student_info.csv','a',newline='') as csv_file:
    writer=csv.writer(csv_file)
  if csv_file.tell()==0:
    writer.writerow(['Name','Age','Contact Number','Email ID'])
    writer.writerow(info_list)
if __name__=='__main__':
  condition=True
  student_num=1
  while condition:
    student_info=input('Enter student information for student #{} in the following format(Name Age Contact_Number E-mail_ID):'.format(student_num))
    student_info_list=student_info.split(' ')
    print('\nThe entered information is-\nName: {0}\nAge: {0}\nContactno: {0}\nEmail ID: {0}'.format(student_info_list))
    choice_check=input('IS the entered information correct? (yes/no): ')
    if choice_check=='yes':
      write_into_csv(student_info_list)

      condition_check=input('Enter (yes/no) if you want to enter the information of another student: ')
        if condition_check=='yes':
           condition=True
           student_num+=1 
        elif condition_check=='no':
            condition=False
    elif choice_Check=='no':
       print('\nRe-enter the values!')
