import os
import pymysql.cursors
import json
import subprocess
insplit=[]

# #Input from user via mic
# user_input=input("Enter your command:")
def execute_commands(user_query):
    #Invalid words which will be removed
    invalid_words=['a','an','the','is','am','are','this','that','do','please','would','you','of','me','could','show','present','my','what','who','me','my','','tell','hey','all','in','under','then','will','would','for','there','command','find','my','run','execute','tell','year']
    connectionObject=pymysql.connect(host='127.0.0.1',user='root',password='2002',database='speech_recognition',charset='utf8mb4'
    ,cursorclass=pymysql.cursors.DictCursor)

    #conerting input string to list
    user_input_list=user_query.split()

    try:
        #creating a cursor object
        cursorObject=connectionObject.cursor()

        #creating list after removing inappropriate words
        for my_val in user_input_list:
            if my_val not in invalid_words:
                insplit.append(my_val)

        #converting list to string
        insplit_str=' '.join(insplit)
        #print(insplit_str)
        #to check whether user has given the command for creating a directory or file
        if(insplit_str.startswith('make') | insplit_str.startswith('create')):
            if('directory' in insplit_str):
                path=insplit_str.split()
                #print(path)
                pathvar=path[2:]
                str='/'.join(pathvar)
                command="mkdir /"+str
                #print(command)
                proc = subprocess.Popen([command], stdout=subprocess.PIPE, shell=True)
                (out, err) = proc.communicate()
                print(out.decode())

            elif('file' in insplit_str):
                path=insplit_str.split()
                pathvar=path[2:]
                str='/'.join(pathvar)
                command ="touch /"+str
                #print(command)
                proc = subprocess.Popen([command], stdout=subprocess.PIPE, shell=True)
                (out, err) = proc.communicate()
                print(out.decode())

        elif(insplit_str.startswith('remove') | insplit_str.startswith('delete')):
            if('directory' in insplit_str):
                path=insplit_str.split()
                pathvar=path[2:]
                str='/'.join(pathvar)
                command="rm -rvf /"+str
                #print(command)
                proc = subprocess.Popen([command], stdout=subprocess.PIPE, shell=True)
                (out, err) = proc.communicate()
                print(out.decode())

            elif('file' in insplit_str):
                path=insplit_str.split()
                pathvar=path[2:]
                str='/'.join(pathvar)
                command="rm -rvf /"+str
                #print(command)
                proc = subprocess.Popen([command], stdout=subprocess.PIPE, shell=True)
                (out, err) = proc.communicate()
                print(out.decode())

        #for calendar command
        elif(insplit_str.startswith('calendar')):

            #calendar command with year
            if(len(insplit_str)>=9):
                year=insplit_str[9:]
                command="cal "+year
                os.system(command)
            else:
                #without year
                os.system('cal')
        elif(insplit_str.startswith('copy')):
            ind_list=[]
            #print(insplit_str)
            index_to=insplit_str.index(' to')
            index_from=insplit_str.index('from')
            source_path=insplit_str[index_from+5:index_to]
            destination_path=insplit_str[index_to+3:]
            #print(source_path)
            # print(destination_path)
            source_list=source_path.split()
            source_command='/'.join(source_list)
            #print(source_command)
            destination_list=destination_path.split()
            destination_command='/'.join(destination_list)
            #print(destination_command)
            final_command="sudo cp /"+source_command+" /"+destination_command
            #print(final_command)
            proc = subprocess.Popen([final_command], stdout=subprocess.PIPE, shell=True)
            (out, err) = proc.communicate()
            print(out.decode())


        elif(insplit_str.startswith('move')):
            ind_list=[]
            #print(insplit_str)
            index_to=insplit_str.index(' to')
            index_from=insplit_str.index('from')
            source_path=insplit_str[index_from+5:index_to]
            destination_path=insplit_str[index_to+3:]
            #print(source_path)
            # print(destination_path)
            source_list=source_path.split()
            source_command='/'.join(source_list)
            #print(source_command)
            destination_list=destination_path.split()
            destination_command='/'.join(destination_list)
            #print(destination_command)
            # proc = subprocess.Popen(['whoami'], stdout=subprocess.PIPE, shell=True)
            # (out, err) = proc.communicate()
            # user=out.decode()
            final_command="sudo mv /"+source_command+" /"+destination_command
            #print(final_command)
            proc = subprocess.Popen([final_command], stdout=subprocess.PIPE, shell=True)
            (out, err) = proc.communicate()
            print(out.decode())

        else:

            #SQL Query
            var='"'+insplit_str+'"'
            sqlQuery="select command from commands where user_input="+var
            #print(sqlQuery)

            #executing sql query
            cursorObject.execute(sqlQuery)

            #fetching data from sql
            rows=cursorObject.fetchall()
            dict=rows[0]
            val=list(dict.values())
            inp=val[0]
            #os.system(inp)
            s=''.join(val)
            proc = subprocess.Popen([inp], stdout=subprocess.PIPE, shell=True)
            (out, err) = proc.communicate()
            print(out.decode())
            #print(var12)

    except Exception as e:
        #Exception Caught
        print("Exception Occured")

    finally:
        #CLosing the connection
        connectionObject.close()
        return
