"""Service module 41530: business logic, no crypto."""


def calculate_total_41530(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41530():
    return 'module 41530 handles orders and invoices'
