"""Service module 40666: business logic, no crypto."""


def calculate_total_40666(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40666():
    return 'module 40666 handles orders and invoices'
