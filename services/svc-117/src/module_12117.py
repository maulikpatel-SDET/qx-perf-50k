"""Service module 12117: business logic, no crypto."""


def calculate_total_12117(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12117():
    return 'module 12117 handles orders and invoices'
