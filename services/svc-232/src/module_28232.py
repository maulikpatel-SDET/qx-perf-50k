"""Service module 28232: business logic, no crypto."""


def calculate_total_28232(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28232():
    return 'module 28232 handles orders and invoices'
