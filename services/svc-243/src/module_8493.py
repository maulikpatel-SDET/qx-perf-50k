"""Service module 8493: business logic, no crypto."""


def calculate_total_8493(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8493():
    return 'module 8493 handles orders and invoices'
