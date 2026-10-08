"""Service module 41493: business logic, no crypto."""


def calculate_total_41493(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41493():
    return 'module 41493 handles orders and invoices'
