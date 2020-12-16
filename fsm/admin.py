from django.contrib import admin
from .models import *


class EdgeAdmin(admin.ModelAdmin):
    model = FSMEdge
    list_display = ['text', 'priority', 'head_name', 'tail_name']

    def head_name(self, obj):
        name = obj.head.name
        return name

    def tail_name(self, obj):
        name = obj.tail.name
        return name

    head_name.short_description = "سر یال"
    tail_name.short_description = "ته یال "


class AnswerAdmin(admin.ModelAdmin):
    model = UploadFileAnswer
    list_display = ['id', 'answer_file', ]

    # def name(self, obj):
    #     name = obj.problem.name
    #     return name


class SubmittedAnswerAdmin(admin.ModelAdmin):
    model = UploadFileAnswer
    list_display = ['name', 'answer_file', 'team_name']

    def name(self, obj):
        name = obj.problem.name
        return name

    def answer_file(self, obj):
        ans_file = obj.answer.uploadfileanswer.answer_file


    def team_name(self, obj):
        return str(obj.player.team.group_name)


class PlayerWorkshopAdmin(admin.ModelAdmin):
    model = PlayerWorkshop
    list_display = ['player', 'workshop', 'current_state', 'last_visit']

    # def name(self, obj):
    #     name = obj.problem.name
    #     return name
    #
    # def answer_file(self, obj):
    #     ans_file = obj.answer.uploadfileanswer.answer_file
    #
    #
    # def team_name(self, obj):
    #     return str(obj.player.team.group_name)


admin.site.register(FSM)
admin.site.register(FSMEdge, EdgeAdmin)
admin.site.register(Ability)
admin.site.register(FSMState)
admin.site.register(MainState)
admin.site.register(HelpState)
admin.site.register(Widget)
admin.site.register(Game)
admin.site.register(ProblemSmallAnswer)
admin.site.register(SmallAnswer)
admin.site.register(ProblemBigAnswer)
admin.site.register(BigAnswer)
admin.site.register(ProblemMultiChoice)
admin.site.register(MultiChoiceAnswer)
admin.site.register(Choice)
admin.site.register(Answer)
admin.site.register(Article)
admin.site.register(UploadFileAnswer, AnswerAdmin)
admin.site.register(ProblemUploadFileAnswer)
admin.site.register(SubmittedAnswer, SubmittedAnswerAdmin)


admin.site.register(PlayerHistory)
admin.site.register(PlayerWorkshop, PlayerWorkshopAdmin)
