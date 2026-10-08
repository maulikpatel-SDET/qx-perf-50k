"""Service module 32081: business logic, no crypto."""


def calculate_total_32081(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32081():
    return 'module 32081 handles orders and invoices'
