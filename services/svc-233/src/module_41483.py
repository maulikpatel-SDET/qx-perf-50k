"""Service module 41483: business logic, no crypto."""


def calculate_total_41483(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41483():
    return 'module 41483 handles orders and invoices'
