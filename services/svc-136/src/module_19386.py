"""Service module 19386: business logic, no crypto."""


def calculate_total_19386(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19386():
    return 'module 19386 handles orders and invoices'
