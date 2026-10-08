"""Service module 25805: business logic, no crypto."""


def calculate_total_25805(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25805():
    return 'module 25805 handles orders and invoices'
