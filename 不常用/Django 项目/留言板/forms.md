
```python
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '请输入姓名....', 'id':'name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'请输入邮箱....', 'id':'email'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'placeholder': '请输入内容....', id: 'content'}))

    SUGGEST = 'suggest'
    CATEGORY_ITEM = (
        ('SUGGEST', '建议'),
        ('VERYGOOD', '好评'),
    )
    category = forms.ChoiceField(choices=CATEGORY_ITEM)
```
