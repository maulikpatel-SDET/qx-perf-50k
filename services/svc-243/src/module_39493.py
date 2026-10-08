"""Service module 39493: business logic, no crypto."""


def calculate_total_39493(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39493():
    return 'module 39493 handles orders and invoices'
