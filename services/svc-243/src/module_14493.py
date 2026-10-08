"""Service module 14493: business logic, no crypto."""


def calculate_total_14493(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14493():
    return 'module 14493 handles orders and invoices'
