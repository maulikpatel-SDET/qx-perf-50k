"""Service module 15059: business logic, no crypto."""


def calculate_total_15059(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15059():
    return 'module 15059 handles orders and invoices'
