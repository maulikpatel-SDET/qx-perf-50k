"""Service module 2025: business logic, no crypto."""


def calculate_total_2025(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2025():
    return 'module 2025 handles orders and invoices'
