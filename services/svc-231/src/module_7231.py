"""Service module 7231: business logic, no crypto."""


def calculate_total_7231(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7231():
    return 'module 7231 handles orders and invoices'
