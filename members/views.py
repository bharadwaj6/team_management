# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import generics

from .models import Member
from .serializers import MemberSerializer


class MemberList(generics.ListCreateAPIView):
    """To create new members and to return a list of all existing members.

    GET => list of all members
    POST => create new members
    """

    queryset = Member.objects.all()
    serializer_class = MemberSerializer


class MemberDetail(generics.RetrieveUpdateDestroyAPIView):
    """To fetch, update and delete existing members.

    GET => show details of a member
    POST => update all details of a member
    PATCH => partial update for details of a member
    DELETE => delete a member
    """

    queryset = Member.objects.all()
    serializer_class = MemberSerializer
