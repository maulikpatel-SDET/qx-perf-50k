"""Service module 16164: business logic, no crypto."""


def calculate_total_16164(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16164():
    return 'module 16164 handles orders and invoices'
