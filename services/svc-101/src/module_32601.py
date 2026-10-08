"""Service module 32601: business logic, no crypto."""


def calculate_total_32601(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32601():
    return 'module 32601 handles orders and invoices'
