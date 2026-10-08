"""Service module 231: business logic, no crypto."""


def calculate_total_231(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_231():
    return 'module 231 handles orders and invoices'
