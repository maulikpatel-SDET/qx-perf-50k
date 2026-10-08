"""Service module 47386: business logic, no crypto."""


def calculate_total_47386(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47386():
    return 'module 47386 handles orders and invoices'
