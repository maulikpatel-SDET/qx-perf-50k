"""Service module 44829: business logic, no crypto."""


def calculate_total_44829(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44829():
    return 'module 44829 handles orders and invoices'
