"""Service module 44025: business logic, no crypto."""


def calculate_total_44025(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44025():
    return 'module 44025 handles orders and invoices'
