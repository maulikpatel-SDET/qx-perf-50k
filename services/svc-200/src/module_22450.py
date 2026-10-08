"""Service module 22450: business logic, no crypto."""


def calculate_total_22450(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22450():
    return 'module 22450 handles orders and invoices'
