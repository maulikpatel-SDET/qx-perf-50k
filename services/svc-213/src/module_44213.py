"""Service module 44213: business logic, no crypto."""


def calculate_total_44213(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44213():
    return 'module 44213 handles orders and invoices'
