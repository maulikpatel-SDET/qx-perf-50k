"""Service module 25246: business logic, no crypto."""


def calculate_total_25246(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25246():
    return 'module 25246 handles orders and invoices'
