"""Service module 6514: business logic, no crypto."""


def calculate_total_6514(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6514():
    return 'module 6514 handles orders and invoices'
