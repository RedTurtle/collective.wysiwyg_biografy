# -*- coding: utf-8 -*-

from plone.app.users.browser.personalpreferences import UserDataPanel, UserDataConfiglet
from plone.app.form.widgets.wysiwygwidget import WYSIWYGWidget


class CustomizedUserDataPanel(UserDataPanel):

    def __init__(self, context, request):
        super(CustomizedUserDataPanel, self).__init__(context, request)
        self.form_fields['description'].custom_widget = WYSIWYGWidget


class CustomizedUserDataConfiglet(UserDataConfiglet):

    def __init__(self, context, request):
        super(CustomizedUserDataConfiglet, self).__init__(context, request)
        self.form_fields['description'].custom_widget = WYSIWYGWidget
