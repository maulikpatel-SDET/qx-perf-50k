"""Service module 32402: business logic, no crypto."""


def calculate_total_32402(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32402():
    return 'module 32402 handles orders and invoices'
