from tabnanny import check
from django.http import HttpResponse
from django.shortcuts import render
import time
from random import randint

text=''
starttime=time.time()
endtime=time.time()
number_of_word=0
a="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
b='''Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet.."'''
c='''There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text. All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the Internet. It uses a dictionary of over 200 Latin words, combined with a handful of model sentence structures, to generate Lorem Ipsum which looks reasonable. The generated Lorem Ipsum is therefore always free from repetition, injected humour, or non-characteristic words etc.'''
d='''But I must explain to you how all this mistaken idea of denouncing pleasure and praising pain was born and I will give you a complete account of the system, and expound the actual teachings of the great explorer of the truth, the master-builder of human happiness. No one rejects, dislikes, or avoids pleasure itself, because it is pleasure, but because those who do not know how to pursue pleasure rationally encounter consequences that are extremely painful. Nor again is there anyone who loves or pursues or desires to obtain pain of itself, because it is pain, but because occasionally circumstances occur in which toil and pain can procure him some great pleasure. To take a trivial example, which of us ever undertakes laborious physical exercise, except to obtain some advantage from it? But who has any right to find fault with a man who chooses to enjoy a pleasure that has no annoying consequences, or one who avoids a pain that produces no resultant pleasure?'''
e='''At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate non provident, similique sunt in culpa qui officia deserunt mollitia animi, id est laborum et dolorum fuga. Et harum quidem rerum facilis est et expedita distinctio. Nam libero tempore, cum soluta nobis est eligendi optio cumque nihil impedit quo minus id quod maxime placeat facere possimus, omnis voluptas assumenda est, omnis dolor repellendus. Temporibus autem quibusdam et aut officiis debitis aut rerum necessitatibus saepe eveniet ut et voluptates repudiandae sint et molestiae non recusandae. Itaque earum rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus maiores alias consequatur aut perferendis doloribus asperiores repellat'''

text_story=[a,b,c,d,e]

# Create your views here.
def index(request):
    # return HttpResponse("Hello")
    global starttime
    starttime=time.time()
    global text
    abc=randint(0,4)
    text=text_story[abc].strip()
    word_list=text.split(" ")
    global number_of_word
    number_of_word=len(word_list)
    return render(request,"home.html",{"text":text})

def Check(request):
    global endtime
    endtime=time.time()
    if request.method=="POST":
        data=request.POST['text_data']
    word_accuracy=0

    text_list=text.split(" ")
    data_list=str(data).split(" ")
    if len(data_list)<=len(text_list):
        for i in range(0,len(data_list)):
            if data_list[i]==text_list[i]:
                word_accuracy=word_accuracy+1
        acc=word_accuracy/len(data_list)

    else:
        for i in range(0,len(text_list)):
            if data_list[i]==text_list[i]:
                word_accuracy=word_accuracy+1
        acc=word_accuracy/len(text_list)


        
    # if (len(text)>=len(data)):
    #     try:
    #         for i in range(0,len(text)):
    #             if text[i]==data[i]:
    #                 accuracy=accuracy+1

    #     except:
    #         pass
    # else:
    #     for ii in range(0,len(text)):
    #         if(text[ii])==data[ii]:
    #             accuracy=accuracy+1

    # acc=word_accuracy/len(data_list)
    accd=float("{:.2f}".format(acc))*100
    f_acc=(str(accd)+"%")
    time_dif=float("{:.2f}".format(endtime-starttime))
    
    if time_dif>60:

        timemin=int(time_dif/60)
        timesec=int(time_dif%60)
    else:
        timemin="00"
        timesec=int(time_dif)
    time_data=str(timemin)+" minutes  "+str(timesec)+" Second"
    # re=data
    wpm_acc=int((len(str(data).split(" "))/time_dif)*60)
    dic={
        "accurac":f_acc,
        "wpm":wpm_acc,
        "time":time_data,
        "data_recived":data,
        "error":100-int(accd)

    }
    return render(request,"result.html",{"dic":dic})