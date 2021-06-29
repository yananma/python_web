
例子 1  

```python 
def foo(*args, **kwargs):
    print('args = ', args)
    print('kwargs = ', kwargs)
    print('---------------------------------------')

foo(1,2,3,4)
foo(a=1,b=2,c=3)
foo(1,2,3,4, a=1,b=2,c=3)
foo('a', 1, None, a=1, b='2', c=3)

args =  (1, 2, 3, 4)
kwargs =  {}
---------------------------------------
args =  ()
kwargs =  {'a': 1, 'b': 2, 'c': 3}
---------------------------------------
args =  (1, 2, 3, 4)
kwargs =  {'a': 1, 'b': 2, 'c': 3}
---------------------------------------
args =  ('a', 1, None)
kwargs =  {'a': 1, 'b': '2', 'c': 3}
---------------------------------------
```

《流畅的 Python》5.7 节，示例 5-11 敲一遍，就完全弄明白了  

```python
@pysnooper.snoop()
def tag(name, *content, cls=None, **attrs):
    """生成一个或多个 HTML 标签"""
    if cls is not None:
        attrs['class'] = cls
    if attrs:
        attr_str = ''.join('%s="%s" '%(attr, value) for attr, value in sorted(attrs.items()))
    else:
        attr_str = ''
    if content:
        return '\n'.join('<%s %s>%s</%s>'%(name, attr_str, c, name) for c in content)
    else:
        return '<%s %s />'%(name, attr_str)
```
