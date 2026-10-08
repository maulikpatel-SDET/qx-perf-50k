"""Service module 4231: business logic, no crypto."""


def calculate_total_4231(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4231():
    return 'module 4231 handles orders and invoices'
