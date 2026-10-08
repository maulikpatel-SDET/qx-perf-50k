"""Service module 26025: business logic, no crypto."""


def calculate_total_26025(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26025():
    return 'module 26025 handles orders and invoices'
