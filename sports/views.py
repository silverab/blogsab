from django.shortcuts import render
from datetime import datetime, timedelta
from sports.models import LPost, RPost, CPost, MiniCPost, AsiaPost

def home(request):
	asia = AsiaPost.objects.all().order_by('-id')[:3]
	rightpost = RPost.objects.all().order_by('-id')[:1]
	double_rightpost = RPost.objects.all().order_by('-id')[1:3]
	left_singlepost = LPost.objects.all().order_by('-id')[:1]
	left_doublepost = LPost.objects.all().order_by('-id')[1:3]
	center_singlepost = CPost.objects.all().order_by('-id')[:1]
	center_doublepost = CPost.objects.all()[1:3]
	minipost = MiniCPost.objects.all()
	template = 'sports/index.html'
	context = {'leftposts': left_singlepost, 'left_doublesports': left_doublepost, 'rightposts': rightpost, 'cposts': center_singlepost, 'dobuleposts': center_doublepost, 'miniposts': minipost, 'double_rightposts': double_rightpost, 'asia': asia }
	response =  render(request, template, context)
	response.set_signed_cookie('name', 'User', salt='ab' , expires=datetime.utcnow()+timedelta(days=2))
	return response