"""
@Description: Enrollment Apps modules
@Author: Jobet Casquejo
@Group: 
@Last Modified By: Jobet Casquejo
@Last Modifed On: 5/20/2024
Modification Log
Ver     Date        Author          Modification
1.0     5/20/2024   Jobet Casquejo  Initial Version
"""
from django.apps import AppConfig

"""
Class for AppConfig
"""
class EnrollmentConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "enrollment"
