"""Service module 554: business logic, no crypto."""


def calculate_total_554(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_554():
    return 'module 554 handles orders and invoices'
