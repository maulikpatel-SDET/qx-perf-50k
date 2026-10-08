"""Service module 21231: business logic, no crypto."""


def calculate_total_21231(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21231():
    return 'module 21231 handles orders and invoices'
