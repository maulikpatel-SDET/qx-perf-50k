"""Service module 30242: business logic, no crypto."""


def calculate_total_30242(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30242():
    return 'module 30242 handles orders and invoices'
