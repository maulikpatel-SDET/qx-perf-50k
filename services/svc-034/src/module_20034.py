"""Service module 20034: business logic, no crypto."""


def calculate_total_20034(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20034():
    return 'module 20034 handles orders and invoices'
