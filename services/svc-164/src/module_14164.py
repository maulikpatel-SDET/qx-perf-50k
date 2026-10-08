"""Service module 14164: business logic, no crypto."""


def calculate_total_14164(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14164():
    return 'module 14164 handles orders and invoices'
