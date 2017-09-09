from django.shortcuts import render
from django.http import HttpResponse
import random


def index(request):
	response = HttpResponse()
	response.writelines("<h1>Hello Guest</h1>")
	response.write("<p>This is demo of Tuyet Giang</p>")
	return response

def makeColor(request):
	respon = HttpResponse()
	count = 0
	htmlCode = ""
	while (count < 500):
		r = random.randint(0,255)
		g = random.randint(0,255)
		b = random.randint(0,255)
		htmlCode = htmlCode + "<div style='width:50; height: 50; float:left; border-radius:100%; background-color:rgb(" + r +"," + g +"," + b +")'></div>"
		count = count + 1

	respon.write(htmlCode)
	return respon