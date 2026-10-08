"""Service module 48466: business logic, no crypto."""


def calculate_total_48466(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48466():
    return 'module 48466 handles orders and invoices'
