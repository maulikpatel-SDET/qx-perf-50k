"""Service module 16514: business logic, no crypto."""


def calculate_total_16514(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16514():
    return 'module 16514 handles orders and invoices'
