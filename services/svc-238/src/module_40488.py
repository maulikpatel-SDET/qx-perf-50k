"""Service module 40488: business logic, no crypto."""


def calculate_total_40488(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40488():
    return 'module 40488 handles orders and invoices'
