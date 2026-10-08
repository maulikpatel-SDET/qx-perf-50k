"""Service module 18492: business logic, no crypto."""


def calculate_total_18492(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18492():
    return 'module 18492 handles orders and invoices'
