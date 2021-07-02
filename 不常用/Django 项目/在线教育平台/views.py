from django.shortcuts import render
from .forms import NameForm, CommentForm
from .models import Banner, Category, Teacher, XXUser, Course, StarStudent, Blog, Org, Tags, Comment, Person
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.base import View
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from datetime import datetime
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView


# Create your views here.


def test(request):
    if request.method == 'GET':
        form = NameForm()
        # print(form)
        # print({'form':form})
        return render(request, 'test.html', {'form': form})
    if request.method == 'POST':
        person = Person()
        name = request.POST.get('your_name')
        person.name = name
        person.save()
        return HttpResponseRedirect(reverse('index'))



def test1(request):
    if request.method == 'GET':
        form = NameForm()
        return render(request, 'test.html', {'form': form})
    if request.method == 'POST':
        person = Person()
        name = request.POST.get('your_name')
        print(name)
        # person.name = name
        # person.save()
        # return HttpResponseRedirect(reverse('vip'))
        return HttpResponseRedirect('index')


def index(request):
    banner_list = Banner.objects.all()
    category_list = Category.objects.all()[:6]
    blog_list = Blog.objects.all()[:3]
    org_list = Org.objects.all()

    # 数据统计
    teacher_count = Teacher.objects.count()
    course_count = Course.objects.count()
    user_count = XXUser.objects.count()
    category_count = Category.objects.count()
    course_list = Course.objects.order_by('-pub_date').all()
    starstudent_list = StarStudent.objects.all()
    teacher_list = Teacher.objects.all()
    category_id = request.GET.get('category_id')

    # blog = Blog.objects.get(pk=bid)

    ctx = {
        'banner_list':banner_list,
        'category_list':category_list,
        'teacher_count':teacher_count,
        'course_count':course_count,
        'user_count':user_count,
        'category_count':category_count,
        'course_list':course_list,
        'starstudent_list':starstudent_list,
        'blog_list':blog_list,
        'teacher_list':teacher_list,
        'org_list':org_list,
        # 'blog':blog,
        # 'star':star,
    }
    return render(request, 'index.html', ctx)


def course_detail(request, cid):
    course = Course.objects.get(pk=cid)
    course_list = Course.objects.filter(recommend=True)[:3]
    category_list = Category.objects.all()

    ctx = {
        'course':course,
        'course_list':course_list,
        'category_list':category_list,
    }
    return render(request, 'courses-detail.html', ctx)


def course(request):
    course_list = Course.objects.all()
    category_list = Category.objects.all()
    course_count = Course.objects.count()

    category_id = request.GET.get('category_id')

    if category_id:
        course_list = course_list.filter(category_id=category_id)
        category_id = int(category_id)

    try:
        page = request.GET.get('page', 1)
    except PageNotAnInteger:
        page = 1

    p = Paginator(course_list, per_page=1, request=request)

    course_list = p.page(page)

    ctx = {
        'post_list':course_list,
        'category_list':category_list,
        'category_id':category_id,
        'course_count':course_count,
    }

    return render(request, 'courses.html', ctx)


def blog_list(request):
    blog_list = Blog.objects.all()
    latest_blog_list = Blog.objects.order_by('-pub_date').all()[:3]

    try:
        page = request.GET.get('page', 1)
    except PageNotAnInteger:
        page = 1

    p = Paginator(blog_list, per_page=2, request=request)

    course_list = Course.objects.filter(recommend=True)[:3]
    category_list = Category.objects.all()

    tag_list = Tags.objects.all()

    blog_list = p.page(page)
    ctx = {
        'post_list':blog_list,
        'latest_blog_list':latest_blog_list,
        'course_list':course_list,
        'category_list':category_list,
        'tag_list':tag_list,

    }

    return render(request, 'news.html', ctx)


def vip(request):
    # if request.method == 'POST':
        # name = request.POST.get('your_name')
        # print(name)
    return render(request, 'vip.html')


def tag(request, tid):
    tag = Tags.objects.get(pk=tid)
    blog_list = tag.blog_set.all()

    try:
        page = request.GET.get('page', 1)
    except PageNotAnInteger:
        page = 1

    p = Paginator(blog_list, per_page=2, request=request)

    blog_list = p.page(page)

    ctx = {
        'post_list':blog_list,
        'tag':tag,
    }

    return render(request, 'tags.html', ctx)


def comment_del(request, id, bid):
    comment = Comment.objects.get(id=id)
    comment.delete()
    return HttpResponseRedirect(reverse("blog-detail",kwargs={'bid':bid}))



# class CommentUpdate(UpdateView):
#     template_name = 'comment_update.html'
#     model = Comment
#     fields = ['content']
#     success_url = '/blog-detail/1'



def comment_update(request, id, bid):
    form = CommentForm()
    # print(form)
    comment = Comment.objects.get(id=id)
    blog = Blog.objects.get(id=bid)

    if request.method == 'GET':
        # form.content = comment.content
        ctx = {
        'comment':comment,
        'form':form,
        'blog':blog,
        }

        return render(request, 'comment_update.html',ctx)

    if request.method == 'POST':
        # comment = Comment.objects.get(id=id)
        comment.user = request.user
        comment.blog = Blog.objects.get(id=bid)
        comment.content = request.POST.get('comment_text')
        comment.pub_date = datetime.now()
        comment.save()
        return HttpResponseRedirect(reverse("blog-detail",kwargs={'bid':bid}))


        # return render(request, 'news-detail.html')

    # return HttpResponseRedirect(reverse("blog-detail",kwargs={'bid':bid}))


def blog_detail(request, bid):
    form = CommentForm()

    # if request.method == 'POST':
    #     comment = Comment()
    #     comment.user = request.user
    #     comment.blog = Blog.objects.get(id=bid)
    #     comment.content = request.POST.get('comment_text')
    #     comment.pub_date = datetime.now()
        # comment.update(comment.content = request.POST.get('comment_text'))
    #     comment.save()
    #     return HttpResponseRedirect(reverse("blog-detail",kwargs={'bid':bid}))

    blog = Blog.objects.get(pk=bid)
    course_list = Course.objects.filter(recommend=True)[:3]
    category_list = Category.objects.all()
    latest_blog_list = Blog.objects.order_by('pub_date').all()[:3]
    tag_list = Tags.objects.all()
    blog_id = request.GET.get('blog_id')
    # user_id = request.session['user_id']
    comment = Comment()

    ctx = {
        'blog':blog,
        'blog_id':blog_id,
        'latest_blog_list':latest_blog_list,
        'course_list':course_list,
        'category_list':category_list,
        'tag_list':tag_list,
        # 'c_user_id':c_user_id,
        'form':form,
    }
    return render(request, 'news-detail.html', ctx)



def my_logout(request):
    # request.session.pop('user_id')
    # request.session.pop('username')
    logout(request)
    return HttpResponseRedirect(reverse('index'))
    # return render(request, 'index.html')


class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        username = request.POST.get('username')
        print(username)
        password = request.POST.get('password')
        print(password)
        email = request.POST.get('email')

        user = XXUser()
        user.username = username
        user.password = make_password(password)
        user.save()
        print(user.password)
        return HttpResponseRedirect(reverse('login'))



class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            request.session['user_id'] = user.id
            request.session['username'] = user.username
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'login.html', {'error_msg':'用户名或密码错误！'})


class CommentView(View):

    def post(self, request, bid):
        # if 'user_id' not in request.session:
        #     return render(request, 'login.html', {'error_msg':'请先登录再评论'})
        # else:
        comment = Comment()
        comment.user = request.user
        comment.blog = Blog.objects.get(id=bid)
        comment.content = request.POST.get('content')
        comment.pub_date = datetime.now()
        comment.save()
        return HttpResponseRedirect(reverse("blog-detail",kwargs={'bid':bid}))
