"""Service module 17514: business logic, no crypto."""


def calculate_total_17514(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17514():
    return 'module 17514 handles orders and invoices'
