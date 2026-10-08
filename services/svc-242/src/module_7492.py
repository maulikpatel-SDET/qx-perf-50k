"""Service module 7492: business logic, no crypto."""


def calculate_total_7492(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7492():
    return 'module 7492 handles orders and invoices'
