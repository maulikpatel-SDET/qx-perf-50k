"""Service module 49234: business logic, no crypto."""


def calculate_total_49234(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49234():
    return 'module 49234 handles orders and invoices'
