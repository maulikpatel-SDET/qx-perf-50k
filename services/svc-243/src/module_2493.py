"""Service module 2493: business logic, no crypto."""


def calculate_total_2493(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2493():
    return 'module 2493 handles orders and invoices'
