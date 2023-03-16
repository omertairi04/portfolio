from django.shortcuts import render

from .models import Profile , Projects , BlogPosts , Skills

def index(request):
    profile = Profile.objects.all()
    projects = Projects.objects.all()
    blog = BlogPosts.objects.all()
    skills = Skills.objects.all()

    projects_list = []
    for project in projects:
        skills_list = []
        for skill in project.skills.all():
            skills_list.append({'name': skill.name})
        projects_list.append({'title': project.title, 'content': project.content, 'thumbnail': project.thumbnail, 'github': project.github, 'skills': skills_list})

    context = {
        'profile':profile , 
        'projects':projects,
        'blog':blog,
        'skills':skills,
    }

    return render(request , 'index.html' , context)