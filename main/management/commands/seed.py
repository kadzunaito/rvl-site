from datetime import date

from django.core.management.base import BaseCommand

from main.models import (
    Branch,
    LegalDocument,
    NewsItem,
    Proposal,
    Service,
    StructureUnit,
    TrainingProgram,
)


class Command(BaseCommand):
    help = "Seeds the database with default content."

    def handle(self, *args, **options):
        if Service.objects.exists():
            self.stdout.write(self.style.WARNING("Seed data already exists."))
            return

        Service.objects.bulk_create(
            [
                Service(
                    title_ru="Диагностика заболеваний",
                    title_kk="Ауруларды диагностикалау",
                    title_en="Disease diagnostics",
                    description_ru="Бактериология, вирусология, ПЦР и серологические исследования.",
                    description_kk="Бактериология, вирусология, ПТР және серология.",
                    description_en="Bacteriology, virology, PCR, and serological testing.",
                    order=1,
                ),
                Service(
                    title_ru="Контроль безопасности продукции",
                    title_kk="Өнім қауіпсіздігі бақылауы",
                    title_en="Product safety control",
                    description_ru="Исследования кормов, сырья и продукции животноводства.",
                    description_kk="Шикізат, жем және мал өнімдерін зерттеу.",
                    description_en="Testing of feed, raw materials, and livestock products.",
                    order=2,
                ),
                Service(
                    title_ru="Мониторинг и эпизоотия",
                    title_kk="Мониторинг және эпизоотия",
                    title_en="Monitoring and epizootics",
                    description_ru="Аналитика рисков и прогнозирование для регионов.",
                    description_kk="Тәуекелдерді талдау және болжам.",
                    description_en="Risk analytics and forecasting for regions.",
                    order=3,
                ),
            ]
        )

        TrainingProgram.objects.bulk_create(
            [
                TrainingProgram(
                    title_ru="Программы обучения",
                    title_kk="Оқу бағдарламалары",
                    title_en="Training programs",
                    description_ru="Курсы по лабораторной диагностике, биобезопасности и стандартам качества.",
                    description_kk="Диагностика және биологиялық қауіпсіздік курстары.",
                    description_en="Courses on diagnostics, biosafety, and quality standards.",
                    order=1,
                ),
                TrainingProgram(
                    title_ru="Методические базы",
                    title_kk="Әдістемелік база",
                    title_en="Methodology base",
                    description_ru="Электронные пособия, инструкции и база данных исследований.",
                    description_kk="Электрондық оқу құралдары және нұсқаулықтар.",
                    description_en="Digital manuals, instructions, and research database.",
                    order=2,
                ),
            ]
        )

        StructureUnit.objects.bulk_create(
            [
                StructureUnit(
                    title_ru="Центральный аппарат",
                    title_kk="Орталық аппарат",
                    title_en="Central office",
                    description_ru="Методология, управление качеством, аналитика, цифровые сервисы.",
                    description_kk="Әдістеме, сапа менеджменті, аналитика және цифрлық сервистер.",
                    description_en="Methodology, quality management, analytics, digital services.",
                    order=1,
                ),
                StructureUnit(
                    title_ru="Региональные филиалы",
                    title_kk="Өңірлік филиалдар",
                    title_en="Regional branches",
                    description_ru="Выполнение лабораторных исследований и мониторинг эпизоотической ситуации.",
                    description_kk="Зертханалық зерттеулер мен эпизоотиялық мониторинг.",
                    description_en="Laboratory testing and epizootic monitoring.",
                    order=2,
                ),
                StructureUnit(
                    title_ru="Партнерская сеть",
                    title_kk="Серіктес желі",
                    title_en="Partner network",
                    description_ru="Университеты, НИИ и частные лаборатории в проектах национального масштаба.",
                    description_kk="Университеттер мен ғылыми орталықтармен бірлескен жобалар.",
                    description_en="Universities and research institutes in national projects.",
                    order=3,
                ),
            ]
        )

        Branch.objects.bulk_create(
            [
                Branch(
                    name_ru="Астана",
                    name_kk="Астана",
                    name_en="Astana",
                    location_ru="Центральный филиал",
                    location_kk="Орталық филиал",
                    location_en="Central branch",
                    description_ru="Координация исследований и методологическая поддержка регионов.",
                    description_kk="Өңірлерге әдістемелік қолдау және зерттеу үйлестіру.",
                    description_en="Coordination of research and methodological support for regions.",
                ),
                Branch(
                    name_ru="Алматы",
                    name_kk="Алматы",
                    name_en="Almaty",
                    location_ru="Южный филиал",
                    location_kk="Оңтүстік филиал",
                    location_en="Southern branch",
                    description_ru="Диагностика зоонозных заболеваний и мониторинг продукции.",
                    description_kk="Зооноз ауруларын диагностикалау және өнім мониторингі.",
                    description_en="Zoonotic disease diagnostics and product monitoring.",
                ),
            ]
        )

        LegalDocument.objects.bulk_create(
            [
                LegalDocument(
                    title_ru="Ветеринарные правила и инструкции (обновлено 2025)",
                    title_kk="Ветеринариялық ережелер мен нұсқаулықтар (2025)",
                    title_en="Veterinary rules and instructions (2025)",
                    link_url="https://adilet.zan.kz/rus",
                    order=1,
                ),
                LegalDocument(
                    title_ru="План закупок и конкурсов лаборатории",
                    title_kk="Зертхананың сатып алу жоспары",
                    title_en="Laboratory procurement plan",
                    link_url="https://goszakup.gov.kz/",
                    order=2,
                ),
            ]
        )

        NewsItem.objects.bulk_create(
            [
                NewsItem(
                    title_ru="Объявлен конкурс на новый сайт",
                    title_kk="Жаңа сайт конкурсы жарияланды",
                    title_en="Contest for the new website announced",
                    summary_ru="Прием заявок до 30 января, конкурсных работ — до 13 февраля 2026 года.",
                    summary_kk="Өтінімдер 30 қаңтарға дейін, жұмыстар 13 ақпанға дейін қабылданады.",
                    summary_en="Applications due by January 30 and submissions by February 13, 2026.",
                    published_at=date(2026, 1, 28),
                ),
                NewsItem(
                    title_ru="Обновление методических рекомендаций",
                    title_kk="Әдістемелік ұсыныстар жаңартылды",
                    title_en="Methodological guidance updated",
                    summary_ru="Введены новые протоколы по лабораторной диагностике особо опасных заболеваний.",
                    summary_kk="Қауіпті аурулар бойынша жаңа протоколдар енгізілді.",
                    summary_en="New protocols for high-risk diseases were introduced.",
                    published_at=date(2026, 1, 22),
                ),
            ]
        )

        Proposal.objects.bulk_create(
            [
                Proposal(
                    title_ru="Цифровая витрина услуг",
                    title_kk="Қызметтер витринасы",
                    title_en="Digital service showcase",
                    description_ru="Онлайн-калькулятор стоимости, подача заявок и отслеживание статуса.",
                    description_kk="Онлайн-калькулятор және өтінім қадағалау.",
                    description_en="Online cost calculator, submission, and status tracking.",
                ),
                Proposal(
                    title_ru="Админ-панель и CMS",
                    title_kk="Әкімшілік панель",
                    title_en="Admin panel and CMS",
                    description_ru="Модульное управление контентом, роли пользователей и редактура новостей.",
                    description_kk="Контентті басқару және жаңалықтарды редакциялау.",
                    description_en="Modular content management and news editing.",
                ),
            ]
        )

        self.stdout.write(self.style.SUCCESS("Seed data created."))
