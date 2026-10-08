"""Service module 26514: business logic, no crypto."""


def calculate_total_26514(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26514():
    return 'module 26514 handles orders and invoices'
