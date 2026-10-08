"""Service module 32394: business logic, no crypto."""


def calculate_total_32394(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32394():
    return 'module 32394 handles orders and invoices'
