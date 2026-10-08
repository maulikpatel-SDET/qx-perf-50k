"""Service module 30231: business logic, no crypto."""


def calculate_total_30231(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30231():
    return 'module 30231 handles orders and invoices'
