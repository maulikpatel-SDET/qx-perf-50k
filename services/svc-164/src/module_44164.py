"""Service module 44164: business logic, no crypto."""


def calculate_total_44164(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44164():
    return 'module 44164 handles orders and invoices'
