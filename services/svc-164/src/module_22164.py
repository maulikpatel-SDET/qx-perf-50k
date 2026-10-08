"""Service module 22164: business logic, no crypto."""


def calculate_total_22164(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22164():
    return 'module 22164 handles orders and invoices'
