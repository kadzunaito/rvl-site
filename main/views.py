from django.contrib import messages
from django.db.models import Q
from django.shortcuts import redirect, render

from .forms import FeedbackForm
from .models import (
    AccreditationItem,
    Branch,
    DocumentCategory,
    DocumentEntry,
    FAQItem,
    KPI,
    LegalDocument,
    NewsItem,
    Proposal,
    Service,
    StructureUnit,
    TrainingProgram,
    Vacancy,
)
from .translations import TEXT


def home(request, lang="ru"):
    context = _build_context(request, lang, "home")
    if not isinstance(context, dict):
        return context
    return render(request, "main/index.html", context)


def about(request, lang="ru"):
    context = _build_context(request, lang, "about")
    if not isinstance(context, dict):
        return context
    return render(request, "main/about.html", context)


def structure(request, lang="ru"):
    context = _build_context(request, lang, "structure")
    if not isinstance(context, dict):
        return context
    return render(request, "main/structure.html", context)


def services(request, lang="ru"):
    context = _build_context(request, lang, "services")
    if not isinstance(context, dict):
        return context
    return render(request, "main/services.html", context)


def documents(request, lang="ru"):
    context = _build_context(request, lang, "documents")
    if not isinstance(context, dict):
        return context
    return render(request, "main/documents.html", context)


def training(request, lang="ru"):
    context = _build_context(request, lang, "training")
    if not isinstance(context, dict):
        return context
    return render(request, "main/training.html", context)


def legal(request, lang="ru"):
    context = _build_context(request, lang, "legal")
    if not isinstance(context, dict):
        return context
    query = request.GET.get("q", "").strip()
    legal_documents = context["legal_documents"]
    if query:
        legal_documents = legal_documents.filter(
            Q(title_ru__icontains=query)
            | Q(title_kk__icontains=query)
            | Q(title_en__icontains=query)
        )
    context.update({"legal_documents": legal_documents, "query": query})
    return render(request, "main/legal.html", context)


def news(request, lang="ru"):
    context = _build_context(request, lang, "news")
    if not isinstance(context, dict):
        return context
    query = request.GET.get("q", "").strip()
    news_items = context["news_items"]
    if query:
        news_items = news_items.filter(
            Q(title_ru__icontains=query)
            | Q(title_kk__icontains=query)
            | Q(title_en__icontains=query)
            | Q(summary_ru__icontains=query)
            | Q(summary_kk__icontains=query)
            | Q(summary_en__icontains=query)
        )
    context.update({"news_items": news_items, "query": query})
    return render(request, "main/news.html", context)


def proposals(request, lang="ru"):
    context = _build_context(request, lang, "proposals")
    if not isinstance(context, dict):
        return context
    return render(request, "main/proposals.html", context)


def quality(request, lang="ru"):
    context = _build_context(request, lang, "quality")
    if not isinstance(context, dict):
        return context
    return render(request, "main/quality.html", context)


def careers(request, lang="ru"):
    context = _build_context(request, lang, "careers")
    if not isinstance(context, dict):
        return context
    return render(request, "main/careers.html", context)


def faq(request, lang="ru"):
    context = _build_context(request, lang, "faq")
    if not isinstance(context, dict):
        return context
    return render(request, "main/faq.html", context)


def dashboard(request, lang="ru"):
    context = _build_context(request, lang, "dashboard")
    if not isinstance(context, dict):
        return context
    return render(request, "main/dashboard.html", context)


def contacts(request, lang="ru"):
    context = _build_context(request, lang, "contacts")
    if not isinstance(context, dict):
        return context
    return render(request, "main/contacts.html", context)


def _build_context(request, lang, page):
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

    return {
        "lang": lang,
        "page": page,
        "text": text,
        "kpis": KPI.objects.all(),
        "services": Service.objects.all(),
        "training_programs": TrainingProgram.objects.all(),
        "legal_documents": LegalDocument.objects.all(),
        "news_items": NewsItem.objects.filter(is_active=True),
        "proposals": Proposal.objects.all(),
        "structure_units": StructureUnit.objects.all(),
        "branches": Branch.objects.all(),
        "document_categories": DocumentCategory.objects.all(),
        "documents": DocumentEntry.objects.select_related("category"),
        "accreditations": AccreditationItem.objects.all(),
        "vacancies": Vacancy.objects.filter(is_active=True),
        "faqs": FAQItem.objects.all(),
        "form": form,
    }


def _apply_form_placeholders(form, text):
    form.fields["name"].widget.attrs["placeholder"] = text["form_name"]
    form.fields["email"].widget.attrs["placeholder"] = "name@example.kz"
    form.fields["subject"].widget.attrs["placeholder"] = text["form_subject"]
    form.fields["message"].widget.attrs["placeholder"] = text["form_message"]
