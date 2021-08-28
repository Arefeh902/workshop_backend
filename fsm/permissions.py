from rest_framework import permissions
from accounts.models import Member, Teamm, Participant


class IsEventModifier(permissions.BasePermission):
    """
    Permission for event's admin to update event
    """
    message = 'You are not this event\'s modifier'

    def has_object_permission(self, request, view, obj):
        return request.user in obj.modifiers


class IsRegistrationFormModifier(permissions.BasePermission):
    """
    Permission for event's admin to update event
    """
    message = 'You are not this registration_form\'s modifier'

    def has_object_permission(self, request, view, obj):
        return (obj.event_or_fsm and request.user in obj.event_or_fsm.modifiers) or request.user == obj.creator


class IsRegistrationReceiptOwner(permissions.BasePermission):
    """
    Permission for registration receipt owner to get
    """
    message = 'You are not this registration receipt\'s owner'

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class IsReceiptsFormModifier(permissions.BasePermission):
    """
    Permission for receipt's registration form modifiers
    """
    message = 'You are not this registration receipt\'s registration form modifier'

    def has_object_permission(self, request, view, obj):
        return request.user in obj.answer_sheet_of.event_or_fsm.modifiers


class IsTeamHead(permissions.BasePermission):
    """
    Permission for team's head
    """
    message = 'You are not this team\'s head'

    def has_object_permission(self, request, view, obj):
        return obj.team_head.user == request.user


class IsInvitationInvitee(permissions.BasePermission):
    """
    Permission for invitation's invitee
    """
    message = 'you are not this invitation\'s invitee'

    def has_object_permission(self, request, view, obj):
        return obj.invitee.user == request.user


class IsTeamMember(permissions.BasePermission):
    """
    Permission for team's members
    """
    message = 'you are not a member of this team'

    def has_object_permission(self, request, view, obj):
        return len(obj.members.filter(user=request.user)) == 1


class MentorPermission(permissions.BasePermission):
    """
    Permission for mentor
    """
    message = 'you are not a mentor of this fsm'

    def has_object_permission(self, request, view, obj):
        return request.user in obj.mentors.all()


class IsStateModifier(permissions.BasePermission):
    """
    Permission for mentors modifying states
    """
    message = 'you are not this state modifier'

    def has_object_permission(self, request, view, obj):
        return request.user in obj.fsm.mentors.all()

# -------------


class ParticipantPermission(permissions.BasePermission):

    def has_permission(self, request, view):

        user = request.user
        try:
            if user.is_participant:
                return True
        except:
            return False
        return False


class ActiveTeamsPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        # user = request.user
        # try:
        #     if user.participant.team.is_team_active():
        #         return True
        # except:
        #     return False
        # return False
        return True


class IsCreatorOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance must have an attribute named `owner`.
        return obj.creator == request.user
