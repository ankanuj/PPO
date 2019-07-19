from django.urls import path
from . import views

urlpatterns = [
	path('ecopolicy/',views.ecopolicy,name='ecopolicy'),
	path('publicwelfare/',views.publicwelfare,name='publicwelfare'),
	path('pmdjy/',views.PMJDY,name='PMJDY'),
	path('JanSuraksha/',views.jansuraksha,name='jansuraksha'),
	path('PMJJBY/',views.pmjjby,name='pmjjby'),
	path('PMSBY/',views.pmsby,name='pmsby'),
	path('APY/',views.apy,name='apy'),
	path('Mudra_Yojana/',views.myj,name='myj'),
	path('Stand_Up_India_Scheme/',views.suis,name='suis'),
	path('Pradhan_Mantri_Vaya_Vandana_Yojana/',views.pmvvyj,name='pmvvyj'),


	
]