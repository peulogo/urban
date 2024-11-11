def introspection_info(obj):
    obj_type = type(obj).__name__
    attributes = dir(obj)
    methods = [attr for attr in attributes if callable(getattr(obj, attr))]
    other_attributes = [attr for attr in attributes if not callable(getattr(obj, attr))]
    module = getattr(obj, '__module__', '__main__')

    doc = getattr(obj, '__doc__', 'No documentation available')
    
    info = {
        'type': obj_type,
        'attributes': other_attributes,
        'methods': methods,
        'module': module,
        'documentation': doc
    }
    
    return info

number_info = introspection_info(42)
print(number_info)

