"""Service module 44197: business logic, no crypto."""


def calculate_total_44197(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44197():
    return 'module 44197 handles orders and invoices'
