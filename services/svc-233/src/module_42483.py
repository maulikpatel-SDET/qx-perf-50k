"""Service module 42483: business logic, no crypto."""


def calculate_total_42483(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42483():
    return 'module 42483 handles orders and invoices'
