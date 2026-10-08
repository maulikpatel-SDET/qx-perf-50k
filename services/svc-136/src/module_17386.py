"""Service module 17386: business logic, no crypto."""


def calculate_total_17386(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17386():
    return 'module 17386 handles orders and invoices'
