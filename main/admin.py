from django.contrib import admin

from .models import (
    Branch,
    FeedbackMessage,
    LegalDocument,
    NewsItem,
    Proposal,
    Service,
    StructureUnit,
    TrainingProgram,
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
    list_display = ("name_ru", "location_ru")


@admin.register(FeedbackMessage)
class FeedbackMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "subject", "created_at")
    readonly_fields = ("created_at", "updated_at")
