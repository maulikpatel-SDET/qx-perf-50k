"""Service module 18483: business logic, no crypto."""


def calculate_total_18483(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18483():
    return 'module 18483 handles orders and invoices'
