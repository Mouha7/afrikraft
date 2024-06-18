from django.shortcuts import redirect, render
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.db.models import Q
from django.contrib.auth import get_user_model, authenticate, login, logout

User = get_user_model()
def register_view(request):
    error = False
    msgEmail = ''
    msgPassword = ''
    if request.method == 'POST':
        username = request.POST.get('username', None)
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        repassword = request.POST.get('repassword', None)
        repassword = request.POST.get('repassword', None)
        profile_picture = request.FILES.get('profile_picture', None)
        date_of_birth = request.POST.get('date_of_birth', None)
        bio = request.POST.get('bio', None)
        
        try:
            validate_email(email)
        except ValidationError:
            error = True
            msgEmail = "Erreur, entrer un email valide !"
        
        if password != repassword and not error:
            error = True
            msgPassword = "Les deux mots de passe ne correspondent pas!"
        
        if not error:
            user = User.objects.filter(Q(email=email) | Q(username=username)).first()
            if user:
                error = True
                msgEmail = "Un utilisateur avec l'email ou le nom d'utilisateur existe déjà!"
        
        if not error:
            user = User(
                username = username,
                email = email,
                bio = bio,
                date_of_birth = date_of_birth
            )
            if profile_picture:
                user.profile_picture = profile_picture
            user.set_password(password)
            user.save()
            return redirect('sign_in_view')
    context = {
        'error': error,
        'msgEmail': msgEmail,
        'msgPassword': msgPassword
    }
    return render(request, 'user/register.html', context)

def sign_in_view(request):
    error = False
    message = ''
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = User.objects.filter(email=email).first()
        if user:
            auth_user = authenticate(username=user.username, password=password)
            if auth_user:
                login(request, auth_user)
                return redirect('/')
            else:
                error = True
                message = "Mot de passe incorrecte!"
        else:
            error = True
            message = "L'utilisateur n'existe pas!"
    return render(request, 'user/login.html', context= {'message': message, 'error': error})

def logout_view(request):
    logout(request)
    return redirect('/')