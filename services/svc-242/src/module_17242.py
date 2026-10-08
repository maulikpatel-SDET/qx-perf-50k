"""Service module 17242: business logic, no crypto."""


def calculate_total_17242(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17242():
    return 'module 17242 handles orders and invoices'
