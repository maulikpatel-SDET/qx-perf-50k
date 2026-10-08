"""Service module 20242: business logic, no crypto."""


def calculate_total_20242(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20242():
    return 'module 20242 handles orders and invoices'
