"""Service module 39059: business logic, no crypto."""


def calculate_total_39059(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39059():
    return 'module 39059 handles orders and invoices'
