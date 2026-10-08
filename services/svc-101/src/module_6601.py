"""Service module 6601: business logic, no crypto."""


def calculate_total_6601(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6601():
    return 'module 6601 handles orders and invoices'
