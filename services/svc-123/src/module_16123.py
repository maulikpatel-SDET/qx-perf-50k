"""Service module 16123: business logic, no crypto."""


def calculate_total_16123(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16123():
    return 'module 16123 handles orders and invoices'
