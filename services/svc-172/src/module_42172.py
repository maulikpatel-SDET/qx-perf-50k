"""Service module 42172: business logic, no crypto."""


def calculate_total_42172(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42172():
    return 'module 42172 handles orders and invoices'
