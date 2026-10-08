"""Service module 24386: business logic, no crypto."""


def calculate_total_24386(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24386():
    return 'module 24386 handles orders and invoices'
