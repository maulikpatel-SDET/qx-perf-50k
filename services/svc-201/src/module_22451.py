"""Service module 22451: business logic, no crypto."""


def calculate_total_22451(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22451():
    return 'module 22451 handles orders and invoices'
