"""Service module 10029: business logic, no crypto."""


def calculate_total_10029(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10029():
    return 'module 10029 handles orders and invoices'
