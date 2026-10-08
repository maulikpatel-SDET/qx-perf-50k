"""Service module 12123: business logic, no crypto."""


def calculate_total_12123(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12123():
    return 'module 12123 handles orders and invoices'
