from django.shortcuts import render
from django.http import HttpResponse
from .models import Facinfo
from .models import Essay
from .models import Music

# Create your views here.

def sub(s1):
    s = Facinfo.objects.get(fCode=1)
    return HttpResponse(
    "<h1>Hello world</>"
    "<h2>Hello world</>"
    f"<a href='https://www.youtube.com/watch?v=d_8BYn42L8w'>..{s}..</a>"
    "<img src='https://github.com/image-rs/image/raw/master/examples/fractal.png'>"
    "<h3>Hello world</>"
    )

def Home(s2):
    return render(s2, "Home.html", {})


def page1(p1):  # 오르막길 선택
    t = Music.objects.get(Music_Name='오르막길')
    l = Music.objects.get(Music_Name='오르막길').Music_Link
    I = Music.objects.get(Music_Name='오르막길').Music_Info
    return HttpResponse(
        f"<h1 style='text-align:center'><b>{t}</b></h1>"
        f"<a href={I}>곡 정보</a><br>"
        f"<a href={l}>유튜브 영상</a><br>"
        "<a href='http://127.0.0.1:8000/'> 홈으로 </a>"
        )


def page2(p2):  # 내가 아니라도 선택
    t = Music.objects.get(Music_Name='내가 아니라도')
    l = Music.objects.get(Music_Name='내가 아니라도').Music_Link
    I = Music.objects.get(Music_Name='내가 아니라도').Music_Info
    return HttpResponse(
        f"<h1 style='text-align:center'><b>{t}</b></h1>"
        f"<a href={I}>곡 정보</a><br>"
        f"<a href={l}>유튜브 영상</a><br>"
        "<a href='http://127.0.0.1:8000/'> 홈으로 </a>"
        )


def page3(p3):  # 그래서 그대는 선택
    t = Music.objects.get(Music_Name='그래서 그대는')
    l = Music.objects.get(Music_Name='그래서 그대는').Music_Link
    I = Music.objects.get(Music_Name='그래서 그대는').Music_Info
    return HttpResponse(
        f"<h1 style='text-align:center'><b>{t}</b></h1>"
        f"<a href={I}>곡 정보</a><br>"
        f"<a href={l}>유튜브 영상</a><br>"
        "<a href='http://127.0.0.1:8000/'> 홈으로 </a>"
        )


def page4(p4):  # 사건의 지평선 선택
    t = Music.objects.get(Music_Name='사건의 지평선')
    l = Music.objects.get(Music_Name='사건의 지평선').Music_Link
    I = Music.objects.get(Music_Name='사건의 지평선').Music_Info
    return HttpResponse(
        f"<h1 style='text-align:center'><b>{t}</b></h1>"  
        f"<a href={I}>곡 정보</a><br>"
        f"<a href={l}>유튜브 영상</a><br>"  
        "<a href='http://127.0.0.1:8000/'> 홈으로 </a>"  
        )


def page5(p5):  # Nxde 선택
    t = Music.objects.get(Music_Name='Nxde')
    l = Music.objects.get(Music_Name='Nxde').Music_Link
    I = Music.objects.get(Music_Name='Nxde').Music_Info
    return HttpResponse(
        f"<h1 style='text-align:center'><b>{t}</b></h1>"
        f"<a href={I}>곡 정보</a><br>"
        f"<a href={l}>유튜브 영상</a><br>"
        "<a href='http://127.0.0.1:8000/'> 홈으로 </a>"
        )