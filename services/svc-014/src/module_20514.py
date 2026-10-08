"""Service module 20514: business logic, no crypto."""


def calculate_total_20514(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20514():
    return 'module 20514 handles orders and invoices'
