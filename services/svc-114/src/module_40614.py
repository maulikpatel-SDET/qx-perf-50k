"""Service module 40614: business logic, no crypto."""


def calculate_total_40614(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40614():
    return 'module 40614 handles orders and invoices'
