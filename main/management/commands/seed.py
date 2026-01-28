from datetime import date

from django.core.management.base import BaseCommand

from main.models import (
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


class Command(BaseCommand):
    help = "Seeds the database with default content."

    def handle(self, *args, **options):
        if Service.objects.exists():
            self.stdout.write(self.style.WARNING("Seed data already exists for services."))
        else:
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

        if not TrainingProgram.objects.exists():
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

        if not StructureUnit.objects.exists():
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

        if not Branch.objects.exists():
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
                        focus_ru="Диагностика",
                        focus_kk="Диагностика",
                        focus_en="diagnostics",
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
                        focus_ru="Мониторинг",
                        focus_kk="Мониторинг",
                        focus_en="monitoring",
                    ),
                ]
            )

        if not KPI.objects.exists():
            KPI.objects.bulk_create(
                [
                    KPI(
                        label_ru="исследований в год",
                        label_kk="жылына зерттеу",
                        label_en="tests per year",
                        value="250K",
                        order=1,
                    ),
                    KPI(
                        label_ru="средний срок ответа",
                        label_kk="орташа жауап уақыты",
                        label_en="average response time",
                        value="48",
                        suffix="ч",
                        order=2,
                    ),
                    KPI(
                        label_ru="регионов охвата",
                        label_kk="қамту өңірлері",
                        label_en="coverage regions",
                        value="17",
                        order=3,
                    ),
                ]
            )

        if not DocumentCategory.objects.exists():
            category_reports = DocumentCategory.objects.create(
                title_ru="Отчеты",
                title_kk="Есептер",
                title_en="Reports",
                order=1,
            )
            category_methods = DocumentCategory.objects.create(
                title_ru="Методические материалы",
                title_kk="Әдістемелік материалдар",
                title_en="Methodology",
                order=2,
            )

            DocumentEntry.objects.bulk_create(
                [
                    DocumentEntry(
                        category=category_reports,
                        title_ru="Годовой отчет 2025",
                        title_kk="2025 жылдық есеп",
                        title_en="Annual report 2025",
                        link_url="https://rvl.kz/ru/",
                        published_at=date(2025, 12, 20),
                    ),
                    DocumentEntry(
                        category=category_methods,
                        title_ru="Методика отбора проб",
                        title_kk="Сынамаларды алу әдістемесі",
                        title_en="Sampling methodology",
                        link_url="https://adilet.zan.kz/rus",
                        published_at=date(2025, 11, 15),
                    ),
                ]
            )

        if not AccreditationItem.objects.exists():
            AccreditationItem.objects.bulk_create(
                [
                    AccreditationItem(
                        title_ru="ISO 17025:2017",
                        title_kk="ISO 17025:2017",
                        title_en="ISO 17025:2017",
                        description_ru="Подтверждена компетентность лаборатории по международному стандарту.",
                        description_kk="Халықаралық стандарт бойынша құзыреттілік расталды.",
                        description_en="Laboratory competence confirmed by international standard.",
                        issued_at=date(2025, 6, 10),
                    ),
                    AccreditationItem(
                        title_ru="Национальная аккредитация",
                        title_kk="Ұлттық аккредитация",
                        title_en="National accreditation",
                        description_ru="Аккредитация РК по приоритетным направлениям исследований.",
                        description_kk="Зерттеу бағыттары бойынша ұлттық аккредитация.",
                        description_en="National accreditation for key research areas.",
                        issued_at=date(2024, 9, 5),
                    ),
                ]
            )

        if not Vacancy.objects.exists():
            Vacancy.objects.bulk_create(
                [
                    Vacancy(
                        title_ru="Инженер-лаборант",
                        title_kk="Зертханашы-инженер",
                        title_en="Laboratory engineer",
                        location_ru="Астана",
                        location_kk="Астана",
                        location_en="Astana",
                        description_ru="Работа с ПЦР, подготовка образцов, ведение отчетности.",
                        description_kk="ПТР, сынама дайындау және есеп жүргізу.",
                        description_en="PCR workflows, sample preparation, reporting.",
                        deadline=date(2026, 2, 28),
                        is_active=True,
                    ),
                    Vacancy(
                        title_ru="Стажер IT",
                        title_kk="IT тағылымгері",
                        title_en="IT intern",
                        location_ru="Алматы",
                        location_kk="Алматы",
                        location_en="Almaty",
                        description_ru="Участие в разработке цифровых сервисов лаборатории.",
                        description_kk="Зертхананың цифрлық сервистеріне қатысу.",
                        description_en="Contribute to digital services development.",
                        deadline=date(2026, 3, 10),
                        is_active=True,
                    ),
                ]
            )

        if not FAQItem.objects.exists():
            FAQItem.objects.bulk_create(
                [
                    FAQItem(
                        question_ru="Как подать заявку на исследование?",
                        question_kk="Зерттеуге өтінім қалай беріледі?",
                        question_en="How to submit a test request?",
                        answer_ru="Свяжитесь с региональным филиалом или отправьте запрос через форму обратной связи.",
                        answer_kk="Өңірлік филиалға хабарласыңыз немесе кері байланыс формасын пайдаланыңыз.",
                        answer_en="Contact a regional branch or use the feedback form.",
                        order=1,
                    ),
                    FAQItem(
                        question_ru="Сколько времени занимает анализ?",
                        question_kk="Талдау қанша уақыт алады?",
                        question_en="How long does testing take?",
                        answer_ru="Срок зависит от типа исследования, среднее время — 48 часов.",
                        answer_kk="Уақыт зерттеу түріне байланысты, орташа 48 сағат.",
                        answer_en="Time depends on the test type, average 48 hours.",
                        order=2,
                    ),
                ]
            )

        if not LegalDocument.objects.exists():
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

        if not NewsItem.objects.exists():
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

        if not Proposal.objects.exists():
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
