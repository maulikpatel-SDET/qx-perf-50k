"""Service module 7164: business logic, no crypto."""


def calculate_total_7164(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7164():
    return 'module 7164 handles orders and invoices'
