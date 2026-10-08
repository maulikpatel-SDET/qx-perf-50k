"""Service module 143: business logic, no crypto."""


def calculate_total_143(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_143():
    return 'module 143 handles orders and invoices'
