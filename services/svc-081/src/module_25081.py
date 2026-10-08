"""Service module 25081: business logic, no crypto."""


def calculate_total_25081(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25081():
    return 'module 25081 handles orders and invoices'
