"""Service module 16386: business logic, no crypto."""


def calculate_total_16386(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16386():
    return 'module 16386 handles orders and invoices'
