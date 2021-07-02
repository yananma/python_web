from django import forms


class NameForm(forms.Form):
    your_name = forms.CharField(label='姓名', max_length=100)

class CommentForm(forms.Form):
    comment_text = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'请输入评论','id':'comment_text','class':'form-control form-input'}))
