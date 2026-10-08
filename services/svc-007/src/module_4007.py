"""Service module 4007: business logic, no crypto."""


def calculate_total_4007(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4007():
    return 'module 4007 handles orders and invoices'
