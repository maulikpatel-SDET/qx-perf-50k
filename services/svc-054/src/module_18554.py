"""Service module 18554: business logic, no crypto."""


def calculate_total_18554(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18554():
    return 'module 18554 handles orders and invoices'
