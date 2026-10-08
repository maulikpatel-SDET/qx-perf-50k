"""Service module 8197: business logic, no crypto."""


def calculate_total_8197(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8197():
    return 'module 8197 handles orders and invoices'
