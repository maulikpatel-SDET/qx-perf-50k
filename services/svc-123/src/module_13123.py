"""Service module 13123: business logic, no crypto."""


def calculate_total_13123(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13123():
    return 'module 13123 handles orders and invoices'
