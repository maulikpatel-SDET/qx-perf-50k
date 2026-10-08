"""Service module 23184: business logic, no crypto."""


def calculate_total_23184(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23184():
    return 'module 23184 handles orders and invoices'
