"""Service module 41315: business logic, no crypto."""


def calculate_total_41315(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41315():
    return 'module 41315 handles orders and invoices'
