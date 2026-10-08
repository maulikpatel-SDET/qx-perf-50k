"""Service module 21514: business logic, no crypto."""


def calculate_total_21514(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21514():
    return 'module 21514 handles orders and invoices'
