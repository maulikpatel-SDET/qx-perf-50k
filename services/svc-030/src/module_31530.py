"""Service module 31530: business logic, no crypto."""


def calculate_total_31530(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31530():
    return 'module 31530 handles orders and invoices'
