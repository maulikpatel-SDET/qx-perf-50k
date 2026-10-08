"""Service module 33514: business logic, no crypto."""


def calculate_total_33514(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33514():
    return 'module 33514 handles orders and invoices'
