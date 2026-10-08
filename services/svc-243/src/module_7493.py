"""Service module 7493: business logic, no crypto."""


def calculate_total_7493(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7493():
    return 'module 7493 handles orders and invoices'
