"""Service module 39643: business logic, no crypto."""


def calculate_total_39643(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39643():
    return 'module 39643 handles orders and invoices'
