"""Service module 28164: business logic, no crypto."""


def calculate_total_28164(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28164():
    return 'module 28164 handles orders and invoices'
