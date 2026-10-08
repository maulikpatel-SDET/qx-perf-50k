"""Service module 7483: business logic, no crypto."""


def calculate_total_7483(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7483():
    return 'module 7483 handles orders and invoices'
