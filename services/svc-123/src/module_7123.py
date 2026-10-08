"""Service module 7123: business logic, no crypto."""


def calculate_total_7123(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7123():
    return 'module 7123 handles orders and invoices'
