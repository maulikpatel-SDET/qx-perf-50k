"""Service module 45594: business logic, no crypto."""


def calculate_total_45594(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45594():
    return 'module 45594 handles orders and invoices'
