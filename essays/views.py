from django.shortcuts import render, get_object_or_404, redirect 
# Create your views here.
from django.http import HttpResponse
from .models import Essay
from .forms import EssayForm
from django.http import Http404
from .word import zuowen, a4
import tempfile
import mimetypes
import os
from docx2pdf import convert

import uuid
def index(request):
    cat = request.GET.get('category', '')
    if cat == '':
        all_essays = Essay.objects.order_by('student_no')
    else:
        all_essays = Essay.objects.filter(category=cat).order_by('student_no')
    context = {'all_essays': all_essays, 'category': cat}
    return render(request, 'essays/index.html', context)

def essay(request, pk):
    essay = get_object_or_404(Essay, uuid=pk)
    return render(request, 'essays/essay.html', {'essay': essay})

def create(request):
    form  = EssayForm(request.POST or None, initial={"category": request.GET.get('category', '第一单元习作')})
    if form.is_valid():
        essay = form.save(commit=False)
        essay.uuid = str(uuid.uuid4())
        essay.save()
        return redirect('essays:essay', essay.uuid)
        #return redirect(request, 'essays/essay.html', {'essay': essay})
    return render(request, 'essays/form.html', {'form': form, 'title': '新增'})
    #return redirect('essays:index')

def update(request, pk):
    essay = get_object_or_404(Essay, uuid=pk)
    form = EssayForm(request.POST or None, instance = essay)
    if form.is_valid():
        form.save()
        return redirect('essays:essay', essay.uuid)
        #return render(request, 'essays/essay.html', {'essay': essay})
    return render(request, 'essays/form.html', {'form': form, 'title': '编辑'})

def delete(request, pk):
    essay = get_object_or_404(Essay, uuid=pk)
    if request.method == 'POST':
        essay.delete()
        return redirect('essays:index')
    return redirect('essays:essay', essay.uuid)
    #return render(request, 'essays/delete.html', {'essay': essay})

def download(request, pk, suffix):
    essay = get_object_or_404(Essay, uuid=pk)
    tmpdir = tempfile.gettempdir()
    file_name = "%d号%s.%s" % (essay.student_no, essay.student_name, suffix)
    doc = zuowen(a4(), essay.student_no, essay.student_name, essay.subject, essay.context)
    full_file = tmpdir+"/"+file_name
    doc.save(full_file)
    path = open(full_file, 'rb')
    mime_type, _ = mimetypes.guess_type(full_file)
    response = HttpResponse(path, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename={0}".format(file_name.encode('utf-8').decode('ISO-8859-1'))  #'java.docx'#% (file_name)
    return response

def download_by_category(request):
    # do filter by category
    cat = request.GET.get('category', '')
    if cat == '':
        cat = '所有文章'
        all_essays = Essay.objects.order_by('student_no')
    else:
        all_essays = Essay.objects.filter(category=cat).order_by('student_no')
    #all_essays = Essay.objects.filter(category=category).order_by('student_no')
    tmpdir = tempfile.gettempdir()
    doc = a4()
    for essay in all_essays:
        doc = zuowen(doc, essay.student_no, essay.student_name, essay.subject, essay.context)
        doc.add_page_break()
    file_name = "%s.%s" %(cat,  "docx")
    full_file = tmpdir+"/"+file_name
    doc.save(full_file)
    path = open(full_file, 'rb')
    mime_type, _ = mimetypes.guess_type(full_file)
    response = HttpResponse(path, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename={0}".format(file_name.encode('utf-8').decode('ISO-8859-1'))
    return response