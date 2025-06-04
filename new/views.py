from django.shortcuts import render
from .forms import UserForm
from .models import UserModel
import openpyxl

def forma_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            foydalanuvchilar = UserModel.objects.all()

            # Excel faylga saqlash
            fayl_nomi = 'foydalanuvchilar.xlsx'
            wb = openpyxl.Workbook()
            ws = wb.active
            ws.append(['first_name', 'last_name', 'Number'])
            for foydalanuvchi in foydalanuvchilar:
                ws.append([foydalanuvchi.first_name, foydalanuvchi.last_name, foydalanuvchi.number])
            wb.save(fayl_nomi)

    else:
        form = UserForm()

    kontekst = {
        'form': form,
        'foydalanuvchilar_soni': UserModel.objects.count()
    }
    return render(request, 'forma.html', kontekst)
