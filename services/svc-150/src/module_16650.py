"""Service module 16650: business logic, no crypto."""


def calculate_total_16650(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16650():
    return 'module 16650 handles orders and invoices'
