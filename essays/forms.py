from django import forms
from .models import Essay

class EssayForm(forms.ModelForm):
    student_name = forms.CharField(
        label="学生姓名",
        widget=forms.TextInput(attrs={'placeholder': '请输入学生姓名'}),
        error_messages={
            "required": "不能为空",
            "invalid": "格式错误"
        })
    student_no = forms.IntegerField(
        label="学号",
        widget=forms.TextInput(attrs={'placeholder': '请输入学号'}),
        error_messages={
            "required": "不能为空",
            "invalid": "格式错误"
        })
    category = forms.CharField(
        label="分类",
        widget=forms.TextInput(attrs={'placeholder': '请输入习作分类'}),
        error_messages={
            "required": "不能为空",
            "invalid": "格式错误"
        })
    subject = forms.CharField(
        label="习作题目",
        widget=forms.TextInput(attrs={'placeholder': '请输入习作题目'}),
        error_messages={
            "required": "不能为空",
            "invalid": "格式错误"
        })
    context = forms.CharField(
        label="文章内容",
        widget=forms.Textarea(attrs={'placeholder': '请输入文章内容', 'cols': '50', 'rows': '10'}),
        error_messages={
            "required": "不能为空",
            "invalid": "格式错误"
        })
    class Meta:
        model = Essay
        fields = ['student_name', 'student_no', 'category', 'subject', 'context']