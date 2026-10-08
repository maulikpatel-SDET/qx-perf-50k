"""Service module 25059: business logic, no crypto."""


def calculate_total_25059(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25059():
    return 'module 25059 handles orders and invoices'
