"""Service module 9492: business logic, no crypto."""


def calculate_total_9492(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9492():
    return 'module 9492 handles orders and invoices'
