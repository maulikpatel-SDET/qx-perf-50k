"""Service module 3492: business logic, no crypto."""


def calculate_total_3492(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3492():
    return 'module 3492 handles orders and invoices'
