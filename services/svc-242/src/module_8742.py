"""Service module 8742: business logic, no crypto."""


def calculate_total_8742(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8742():
    return 'module 8742 handles orders and invoices'
