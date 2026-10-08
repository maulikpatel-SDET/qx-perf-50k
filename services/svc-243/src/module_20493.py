"""Service module 20493: business logic, no crypto."""


def calculate_total_20493(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20493():
    return 'module 20493 handles orders and invoices'
