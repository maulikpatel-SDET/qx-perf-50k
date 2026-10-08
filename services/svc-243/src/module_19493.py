"""Service module 19493: business logic, no crypto."""


def calculate_total_19493(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19493():
    return 'module 19493 handles orders and invoices'
