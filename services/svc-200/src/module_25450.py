"""Service module 25450: business logic, no crypto."""


def calculate_total_25450(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25450():
    return 'module 25450 handles orders and invoices'
