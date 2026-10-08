"""Service module 34123: business logic, no crypto."""


def calculate_total_34123(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34123():
    return 'module 34123 handles orders and invoices'
