"""Service module 47998: business logic, no crypto."""


def calculate_total_47998(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47998():
    return 'module 47998 handles orders and invoices'
