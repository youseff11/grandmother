from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Category, Phrase, Person
from .serializers import CategorySerializer, PhraseSerializer, PersonSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """API للتصنيفات - عرض وإضافة وتعديل وحذف"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class PhraseViewSet(viewsets.ModelViewSet):
    """API للجمل - عرض وإضافة وتعديل وحذف"""
    queryset = Phrase.objects.all()
    serializer_class = PhraseSerializer

    def get_queryset(self):
        queryset = Phrase.objects.all()
        category = self.request.query_params.get('category')
        if category:
            if category.isdigit():
                queryset = queryset.filter(category_id=category)
            else:
                queryset = queryset.filter(category__name=category)
        return queryset


class PersonViewSet(viewsets.ModelViewSet):
    """API للأشخاص - عرض وإضافة وتعديل وحذف"""
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


@api_view(['POST'])
def seed_data(request):
    """إضافة بيانات أولية (أول مرة بس)"""
    if Category.objects.exists():
        return Response({'message': 'البيانات موجودة بالفعل'}, status=status.HTTP_200_OK)

    # إنشاء التصنيفات
    categories_data = [
        {'name': 'أكل وشرب', 'order': 0},
        {'name': 'صحة', 'order': 1},
        {'name': 'مشاعر', 'order': 2},
        {'name': 'طلبات', 'order': 3},
        {'name': 'أماكن', 'order': 4},
        {'name': 'عام', 'order': 5},
    ]

    categories = {}
    for cat_data in categories_data:
        cat = Category.objects.create(**cat_data)
        categories[cat.name] = cat

    # إنشاء الجمل
    phrases = [
        Phrase(text='عايزة مية', category=categories['أكل وشرب'], order=0),
        Phrase(text='عايزة شاي', category=categories['أكل وشرب'], order=1),
        Phrase(text='أنا جعانة', category=categories['أكل وشرب'], order=2),
        Phrase(text='مش عايزة آكل', category=categories['أكل وشرب'], order=3),
        Phrase(text='أنا تعبانة', category=categories['صحة'], order=0),
        Phrase(text='عايزة الدكتور', category=categories['صحة'], order=1),
        Phrase(text='عايزة الدوا', category=categories['صحة'], order=2),
        Phrase(text='رأسي بتوجعني', category=categories['صحة'], order=3),
        Phrase(text='عايزة أنام', category=categories['صحة'], order=4),
        Phrase(text='أنا كويسة', category=categories['مشاعر'], order=0),
        Phrase(text='أنا فرحانة', category=categories['مشاعر'], order=1),
        Phrase(text='وحشتوني', category=categories['مشاعر'], order=2),
        Phrase(text='أنا زعلانة', category=categories['مشاعر'], order=3),
        Phrase(text='بحبكم', category=categories['مشاعر'], order=4),
        Phrase(text='عايزة أروح الحمام', category=categories['طلبات'], order=0),
        Phrase(text='ممكن تساعدوني', category=categories['طلبات'], order=1),
        Phrase(text='افتحوا التكييف', category=categories['طلبات'], order=2),
        Phrase(text='أنا عايزة أقعد', category=categories['طلبات'], order=3),
        Phrase(text='نادوا لي حد', category=categories['طلبات'], order=4),
        Phrase(text='شكراً', category=categories['عام'], order=0),
        Phrase(text='أيوه', category=categories['عام'], order=1),
        Phrase(text='لأ', category=categories['عام'], order=2),
        Phrase(text='مش فاهمة', category=categories['عام'], order=3),
        Phrase(text='السلام عليكم', category=categories['عام'], order=4),
    ]

    Phrase.objects.bulk_create(phrases)
    return Response({'message': 'تم إضافة البيانات الأولية بنجاح'}, status=status.HTTP_201_CREATED)