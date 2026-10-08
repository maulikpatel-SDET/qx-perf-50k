"""Service module 42274: business logic, no crypto."""


def calculate_total_42274(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42274():
    return 'module 42274 handles orders and invoices'
