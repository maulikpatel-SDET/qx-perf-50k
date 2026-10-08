"""Service module 25123: business logic, no crypto."""


def calculate_total_25123(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25123():
    return 'module 25123 handles orders and invoices'
