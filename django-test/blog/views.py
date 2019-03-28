from django.shortcuts import render

# Create your views here.
posts = [
	{
		'author': 'Jisu',
		'title': 'Initial Post',
		'content': 'WAOW',
		'date_posted': '30.March.2019'
	},
	{
		'author': 'Jisu2',
		'title': 'Initial Post2',
		'content': 'WAOW2',
		'date_posted': '32.March.2019'
	}
]


def home(request):
	context = {
		'posts': posts
	}
	return render(request, 'blog/home.html', context)
	
	
def about(request):
	return render(request, 'blog/about.html', {'title': 'About'})
