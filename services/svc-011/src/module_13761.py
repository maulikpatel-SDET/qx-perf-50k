"""Service module 13761: business logic, no crypto."""


def calculate_total_13761(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13761():
    return 'module 13761 handles orders and invoices'
