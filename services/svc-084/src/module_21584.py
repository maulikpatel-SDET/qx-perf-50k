"""Service module 21584: business logic, no crypto."""


def calculate_total_21584(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21584():
    return 'module 21584 handles orders and invoices'
