"""Service module 4514: business logic, no crypto."""


def calculate_total_4514(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4514():
    return 'module 4514 handles orders and invoices'
