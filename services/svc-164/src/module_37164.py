"""Service module 37164: business logic, no crypto."""


def calculate_total_37164(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37164():
    return 'module 37164 handles orders and invoices'
