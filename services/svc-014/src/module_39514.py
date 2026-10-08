"""Service module 39514: business logic, no crypto."""


def calculate_total_39514(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39514():
    return 'module 39514 handles orders and invoices'
