"""Service module 38792: business logic, no crypto."""


def calculate_total_38792(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38792():
    return 'module 38792 handles orders and invoices'
