"""Service module 1234: business logic, no crypto."""


def calculate_total_1234(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1234():
    return 'module 1234 handles orders and invoices'
