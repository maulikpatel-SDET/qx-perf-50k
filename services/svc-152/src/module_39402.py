"""Service module 39402: business logic, no crypto."""


def calculate_total_39402(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39402():
    return 'module 39402 handles orders and invoices'
