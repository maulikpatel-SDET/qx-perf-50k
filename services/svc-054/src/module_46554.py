"""Service module 46554: business logic, no crypto."""


def calculate_total_46554(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46554():
    return 'module 46554 handles orders and invoices'
