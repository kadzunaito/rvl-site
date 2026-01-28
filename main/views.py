from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import FeedbackForm
from .models import (
    Branch,
    LegalDocument,
    NewsItem,
    Proposal,
    Service,
    StructureUnit,
    TrainingProgram,
)
from .translations import TEXT


def home(request, lang="ru"):
    if lang not in TEXT:
        lang = "ru"
    text = TEXT[lang]

    form = FeedbackForm(request.POST or None)
    _apply_form_placeholders(form, text)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, text["form_success"])
            return redirect(request.path)
        messages.error(request, text["form_error"])

    context = {
        "lang": lang,
        "text": text,
        "services": Service.objects.all(),
        "training_programs": TrainingProgram.objects.all(),
        "legal_documents": LegalDocument.objects.all(),
        "news_items": NewsItem.objects.filter(is_active=True)[:6],
        "proposals": Proposal.objects.all(),
        "structure_units": StructureUnit.objects.all(),
        "branches": Branch.objects.all()[:6],
        "form": form,
    }
    return render(request, "main/index.html", context)


def _apply_form_placeholders(form, text):
    form.fields["name"].widget.attrs["placeholder"] = text["form_name"]
    form.fields["email"].widget.attrs["placeholder"] = "name@example.kz"
    form.fields["subject"].widget.attrs["placeholder"] = text["form_subject"]
    form.fields["message"].widget.attrs["placeholder"] = text["form_message"]
