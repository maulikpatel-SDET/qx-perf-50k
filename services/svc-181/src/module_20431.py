"""Service module 20431: business logic, no crypto."""


def calculate_total_20431(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20431():
    return 'module 20431 handles orders and invoices'
