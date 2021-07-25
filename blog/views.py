 
from django.shortcuts import redirect, render
from django.http import HttpResponse
from . models import Contact , Post, BlogComment
from django.contrib import messages
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def index(request):
    # allpost = Post.objects.all()
    return render(request,'blog/index.html')

def about(request):
    return render(request,'blog/about.html')

def contact(request):
    
    if request.method=='GET':
        return render(request,'blog/contact.html') 
    else:
        name= request.POST.get('name')  
        phone= request.POST.get('phone')      
        email= request.POST.get('email')      
        desc= request.POST.get('desc')        
        contact = Contact(name=name,phone=phone,email=email,desc=desc)  
        contact.save()
        messages.success(request,'Your message has been sent!')
        return render(request,'blog/contact.html')

     

def blog(request):
    allpost = Post.objects.all()
     
    return render(request,'blog/blog.html',{'allposts':allpost}) 

def blogpost(request, slug ):
     
    post  = Post.objects.filter(slug=slug  ).first() 
    # post.views = post.views+1
    # post.save()
    comments = BlogComment.objects.filter(post=post, parent=None)
    replies = BlogComment.objects.filter(post=post).exclude(parent=None)
    replyDict={}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno]=[reply]
        else:
            replyDict[reply.parent.sno].append(reply)


    # print(comments,replies) 
    # print(replyDict)
    return render(request,'blog/blogpost.html',{'post':post,'comments':comments,'user':request.user,'replyDict':replyDict })



def postcomment(request):
    # allpost = Post.objects.all()
    if request.method=='POST':
        comment = request.POST.get('comment') 
        user = request.user
        postSno  = request.POST.get('postSno')
        parentSno = request.POST.get('parentSno')
        post = Post.objects.get(id=postSno)
        
        if parentSno=="":
            comment = BlogComment(comment=comment, user=user,post=post)
            comment.save()
            messages.success(request,"Your Comment has been sucessfully commented")
        else:
            parent = BlogComment.objects.get(sno=parentSno)
            comment = BlogComment(comment=comment, user=user,post=post,parent=parent )   

            comment.save()
            messages.success(request,"Your Reply has been posted sucessfully" )
    return redirect( f'/blog/{post.slug}' )





def search(request):
    query = request.GET.get('query') 
    allpostTitle = Post.objects.filter(title__icontains=query)
    allpostContent = Post.objects.filter(desc__icontains=query)
    allpostauthor = Post.objects.filter(author__icontains=query)
    allpost = allpostTitle.union(allpostContent).union(allpostauthor)

    return render(request,'blog/search.html',{'allposts':allpost,'query':query} )
     
         

def handleSignup(request):
    if request.method=='POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        # checks?
        if pass1 != pass2:
            messages.error(request,"Password does'nt match")
            return redirect('/')
    #    Create user
        myuser = User.objects.create_user(username,email,pass1) 
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()
        messages.success(request,"Your MyBlog account sucessfully created")
        return redirect('index')
    else:
        return HttpResponse("404 Not Found")       




def handleLogin(request):
    if request.method=='POST':   
        username = request.POST.get('username')
        pass1 = request.POST.get('pass1') 
        user = authenticate(username=username,password=pass1) 
        if user is not None:
            login(request,user)
            messages.success(request,"You are sucessfully Login")
            return redirect('/')
        else:
            messages.error(request,"Invalid Credients")
            return redirect('/')
    else:
        return HttpResponse("404 Not Found")



def handleLogout(request):
    logout(request)
    messages.success(request,"You are successfuly Logout")
    return redirect("/") 



