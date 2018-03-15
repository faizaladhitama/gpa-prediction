from django.shortcuts import render
from api.models import Civitas
from api.models import Mahasiswa
from django.contrib.auth.models import User

# list of mobile User Agents
mobile_uas = [
    'w3c ','acs','alav','amoi','audi','avan','benq','bird','blanc',
    'blaz','brew','cell','cldc','cmd-','dang','doco','eric','hipt','inno',
    'ipaq','java','jigs','kddi','keji','leno','lg-c','lg-d','lg-g','lge-',
    'maui','maxo','midp','mits','mmef','mobi','mot-','moto','mwbp','nec-',
    'newt','noki','oper','palm','pana','pant','phil','play','port','prox',
    'qwap','sage','sams','sany','sch-','sec-','send','seri','sgh-','shar',
    'sie-','siem','smal','smar','sony','sph-','symb','t-mo','teli','tim-',
    'tosh','tsm-','upg1','upsi','vk-v','voda','wap-','wapa','wapi','wapp'
    'wapr','webc','winw','xda','-xda'
]
mobile_ua_hints = ['SymbianOS','Opera Mini','iPhone']
# Create your views here.

def mobileBrowser(request):
    mobile_browser = False
    ua = request.META['HTTP_USER_AGENT'].lower()[0:4]
    if(ua in mobile_uas):
       mobile_browser = True
    else:
       for hint in mobile_ua_hints:
                if(request.META['HTTP_USER_AGENT'].find(hint)>0):
                        mobile_browser = True
    return mobile_browser

def index(request):
    # context : passing args to template
    context = {'team': 'usagi studio'}
    return render(request, 'api/index.tpl', context)


def login(request):
    if request.user == None:
        user = "None"
    else:
        user = request.user
        user_django_id = list(User.objects.filter(username=user))[0].id
        civitas = list(Civitas.objects.filter(user_id=user_django_id))[0]
        mahasiswa = list(Mahasiswa.objects.filter(civitas_ptr_id=civitas.id))[0]
        print(mahasiswa.peran_user)
        context={'team':'usagi studio','user':user,'peran':mahasiswa.peran_user}
        if mobileBrowser(request):
            t = 'mahasiswa/index.tpl'
        else:
            t = 'mahasiswa/mobile/index.tpl'
    return render(request, t ,context)

def landing_page(request):
    #context : passing args to template
    context = {'team':'usagi studio'}
    return render(request, 'landing_page.tpl', context)
