# -*- coding: utf-8 -*-
from drf_yasg import openapi
from drf_yasg.inspectors import SwaggerAutoSchema
from drf_yasg.views import get_schema_view

from rest_framework import permissions


class SwaggerAutoSchemaCustom(SwaggerAutoSchema):
    """ Custom SwaggerAutoSchema """

    def get_operation(self, operation_keys):
        consumes = self.get_consumes()

        body = self.get_request_body_parameters(consumes)
        query = self.get_query_parameters()
        parameters = body + query
        parameters = [param for param in parameters if param is not None]
        parameters = self.add_manual_parameters(parameters)

        operation_id = self.get_operation_id(operation_keys)
        summary, description = self.get_summary_and_description()

        remove_keys = ['create', 'update', 'delete', 'list', 'read', 'partial_update']
        operation_keys = [key for key in operation_keys if key not in remove_keys]

        if len(operation_keys) >= 2:
            tags = ["/".join([item for item in operation_keys])]
        else:
            tags = [operation_keys[-1]]

        responses = self.get_responses()

        return openapi.Operation(
            operation_id=operation_id,
            description=description,
            responses=responses,
            parameters=parameters,
            consumes=consumes,
            tags=tags,
        )


schema_view = get_schema_view(
    openapi.Info(
        title="Front-end Challenge API",
        default_version='v1',
        description="",
        terms_of_service="",
        contact=openapi.Contact(email="tecnologia@keeps.com.br"),
        license=openapi.License(name="BSD License"),
    ),
    validators=[],
    public=True,
    permission_classes=(permissions.AllowAny,),
)
