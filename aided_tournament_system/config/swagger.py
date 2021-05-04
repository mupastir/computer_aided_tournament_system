from drf_yasg import inspectors


class CustomSwaggerSchema(inspectors.SwaggerAutoSchema):
    def get_tags(self, operation_keys=None):
        operation_keys = operation_keys or self.operation_keys

        tags = self.overrides.get("tags")
        if not tags:
            if "api" in operation_keys:
                tags = [f"{operation_keys[2]} api"]
            else:
                tags = [operation_keys[0]]

        return tags
