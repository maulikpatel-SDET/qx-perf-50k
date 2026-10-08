"""Service module 12921: business logic, no crypto."""


def calculate_total_12921(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12921():
    return 'module 12921 handles orders and invoices'
