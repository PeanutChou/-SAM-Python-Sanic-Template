from . import app
from .test import TestView

# 測試路由
app.add_route(TestView.as_view(), "/")