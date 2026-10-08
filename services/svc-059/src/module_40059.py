"""Service module 40059: business logic, no crypto."""


def calculate_total_40059(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40059():
    return 'module 40059 handles orders and invoices'
