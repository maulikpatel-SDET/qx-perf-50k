"""Service module 29231: business logic, no crypto."""


def calculate_total_29231(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29231():
    return 'module 29231 handles orders and invoices'
