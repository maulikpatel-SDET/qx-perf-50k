"""Service module 605: business logic, no crypto."""


def calculate_total_605(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_605():
    return 'module 605 handles orders and invoices'
