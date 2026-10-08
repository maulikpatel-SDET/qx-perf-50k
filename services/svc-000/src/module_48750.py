"""Service module 48750: business logic, no crypto."""


def calculate_total_48750(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48750():
    return 'module 48750 handles orders and invoices'
