"""Service module 49025: business logic, no crypto."""


def calculate_total_49025(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49025():
    return 'module 49025 handles orders and invoices'
