"""Service module 21828: business logic, no crypto."""


def calculate_total_21828(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21828():
    return 'module 21828 handles orders and invoices'
