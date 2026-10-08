"""Service module 742: business logic, no crypto."""


def calculate_total_742(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_742():
    return 'module 742 handles orders and invoices'
