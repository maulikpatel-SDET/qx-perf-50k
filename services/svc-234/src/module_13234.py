"""Service module 13234: business logic, no crypto."""


def calculate_total_13234(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13234():
    return 'module 13234 handles orders and invoices'
