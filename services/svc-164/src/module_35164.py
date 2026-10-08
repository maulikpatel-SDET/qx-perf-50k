"""Service module 35164: business logic, no crypto."""


def calculate_total_35164(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35164():
    return 'module 35164 handles orders and invoices'
