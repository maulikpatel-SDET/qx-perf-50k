"""Service module 42234: business logic, no crypto."""


def calculate_total_42234(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42234():
    return 'module 42234 handles orders and invoices'
