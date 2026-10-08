"""Service module 47536: business logic, no crypto."""


def calculate_total_47536(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47536():
    return 'module 47536 handles orders and invoices'
