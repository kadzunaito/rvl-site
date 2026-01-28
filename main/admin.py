from django.contrib import admin

from .models import (
    AccreditationItem,
    Branch,
    DocumentCategory,
    DocumentEntry,
    FAQItem,
    FeedbackMessage,
    KPI,
    LegalDocument,
    NewsItem,
    Proposal,
    Service,
    StructureUnit,
    TrainingProgram,
    Vacancy,
)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title_ru", "order", "updated_at")
    list_editable = ("order",)
    search_fields = ("title_ru", "title_kk", "title_en")


@admin.register(TrainingProgram)
class TrainingProgramAdmin(admin.ModelAdmin):
    list_display = ("title_ru", "order", "updated_at")
    list_editable = ("order",)


@admin.register(LegalDocument)
class LegalDocumentAdmin(admin.ModelAdmin):
    list_display = ("title_ru", "link_url", "order")
    list_editable = ("order",)


@admin.register(NewsItem)
class NewsItemAdmin(admin.ModelAdmin):
    list_display = ("title_ru", "published_at", "is_active")
    list_filter = ("is_active",)
    search_fields = ("title_ru", "title_kk", "title_en")


@admin.register(Proposal)
class ProposalAdmin(admin.ModelAdmin):
    list_display = ("title_ru", "updated_at")


@admin.register(StructureUnit)
class StructureUnitAdmin(admin.ModelAdmin):
    list_display = ("title_ru", "order")
    list_editable = ("order",)


@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ("name_ru", "location_ru", "focus_ru")


@admin.register(KPI)
class KPIAdmin(admin.ModelAdmin):
    list_display = ("label_ru", "value", "suffix", "order")
    list_editable = ("order",)


@admin.register(DocumentCategory)
class DocumentCategoryAdmin(admin.ModelAdmin):
    list_display = ("title_ru", "order")
    list_editable = ("order",)


@admin.register(DocumentEntry)
class DocumentEntryAdmin(admin.ModelAdmin):
    list_display = ("title_ru", "category", "published_at")
    list_filter = ("category",)


@admin.register(AccreditationItem)
class AccreditationItemAdmin(admin.ModelAdmin):
    list_display = ("title_ru", "issued_at")


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ("title_ru", "location_ru", "deadline", "is_active")
    list_filter = ("is_active",)


@admin.register(FAQItem)
class FAQItemAdmin(admin.ModelAdmin):
    list_display = ("question_ru", "order")
    list_editable = ("order",)


@admin.register(FeedbackMessage)
class FeedbackMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "subject", "created_at")
    readonly_fields = ("created_at", "updated_at")
