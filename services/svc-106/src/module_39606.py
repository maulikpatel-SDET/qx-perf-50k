"""Service module 39606: business logic, no crypto."""


def calculate_total_39606(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39606():
    return 'module 39606 handles orders and invoices'
