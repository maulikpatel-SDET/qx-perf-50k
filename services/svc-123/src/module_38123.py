"""Service module 38123: business logic, no crypto."""


def calculate_total_38123(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38123():
    return 'module 38123 handles orders and invoices'
