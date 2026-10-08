"""Service module 33693: business logic, no crypto."""


def calculate_total_33693(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33693():
    return 'module 33693 handles orders and invoices'
