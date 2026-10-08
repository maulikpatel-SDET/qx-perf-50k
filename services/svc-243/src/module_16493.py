"""Service module 16493: business logic, no crypto."""


def calculate_total_16493(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16493():
    return 'module 16493 handles orders and invoices'
