"""Service module 28402: business logic, no crypto."""


def calculate_total_28402(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28402():
    return 'module 28402 handles orders and invoices'
