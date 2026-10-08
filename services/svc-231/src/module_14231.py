"""Service module 14231: business logic, no crypto."""


def calculate_total_14231(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14231():
    return 'module 14231 handles orders and invoices'
