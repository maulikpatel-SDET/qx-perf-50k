"""Service module 4536: business logic, no crypto."""


def calculate_total_4536(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4536():
    return 'module 4536 handles orders and invoices'
