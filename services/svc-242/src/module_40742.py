"""Service module 40742: business logic, no crypto."""


def calculate_total_40742(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40742():
    return 'module 40742 handles orders and invoices'
