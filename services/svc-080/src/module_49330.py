"""Service module 49330: business logic, no crypto."""


def calculate_total_49330(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49330():
    return 'module 49330 handles orders and invoices'
