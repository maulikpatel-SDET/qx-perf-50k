"""Service module 49176: business logic, no crypto."""


def calculate_total_49176(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49176():
    return 'module 49176 handles orders and invoices'
