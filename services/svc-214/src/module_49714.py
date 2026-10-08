"""Service module 49714: business logic, no crypto."""


def calculate_total_49714(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49714():
    return 'module 49714 handles orders and invoices'
