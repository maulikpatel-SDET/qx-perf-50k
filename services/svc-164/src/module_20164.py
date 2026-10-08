"""Service module 20164: business logic, no crypto."""


def calculate_total_20164(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20164():
    return 'module 20164 handles orders and invoices'
