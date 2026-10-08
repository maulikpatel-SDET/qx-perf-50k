"""Service module 45386: business logic, no crypto."""


def calculate_total_45386(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45386():
    return 'module 45386 handles orders and invoices'
