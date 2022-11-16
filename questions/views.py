from django.shortcuts import render
from random import choice

from static.py.elements import tags, authorized


def paginate(object_list, page, per_page=5):
    first_pos = (page - 1) * per_page
    last_pos = page * per_page
    lst = {
        'page': page,
        'element_count': len(object_list)//per_page + (len(object_list) % per_page),
        'object_list': object_list[first_pos:last_pos],
        'is_end': len(object_list)//per_page + (len(object_list) % per_page) <= page,
        'is_start': page == 1,
        'next': page + 1,
        'next_next': page + 2,
        'list_empty': not bool(object_list[first_pos:last_pos]),
    }
    return lst


def index(request, tag=None, page=1, hot=None):

    question_objects = [{
            'id': i,
            'author': f'Автор {i * 2}',
            'title': f'Вопрос {i + 1}',
            'body': f'{i * "question text "}',
            'last_update': f'Last updated {i} mins ago',
            'tags': [choice(tags)],
            'answers_count': str(i + 1),
            'likes_count': str(i),
            'dislikes_count': str(i),
            'hot': i % 2,
        } for i in range(31)]

    template = 'questions/index.html'
    context = {
        'authorized': authorized,
        'tags_list': tags,
        'tag': tag,
        'hot': hot,
        'questions': paginate(question_objects, page)
    }
    return render(request, template, context)


def new_question(request):
    template = 'questions/new_question.html'
    context = {
        'authorized': authorized,
    }
    return render(request, template, context)


def settings(request):
    template = 'questions/profile_update.html'
    context = {
        'authorized': authorized,
    }
    return render(request, template, context)


def question(request, id: int):
    answer_objects = [{
        'id': i,
        'author': f'Автор {i * 2}',
        'text': f'{i * "текст ответа "}',
        'last_update': f'Last updated {i} mins ago',
        'likes_count': str(i),
        'dislikes_count': str(i),
    } for i in range(10)]

    template = 'questions/question.html'
    context = {
        'authorized': authorized,
        'tags_list': tags,
        'answers': answer_objects,
        'closed': True,
    }
    return render(request, template, context)


def sign_in(request):
    template = 'questions/sign-in.html'
    return render(request, template)


def sign_up(request):
    template = 'questions/sign-up.html'
    return render(request, template)
