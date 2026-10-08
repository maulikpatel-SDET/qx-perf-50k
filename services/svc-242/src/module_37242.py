"""Service module 37242: business logic, no crypto."""


def calculate_total_37242(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37242():
    return 'module 37242 handles orders and invoices'
