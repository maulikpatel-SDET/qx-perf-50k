"""Service module 38793: business logic, no crypto."""


def calculate_total_38793(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38793():
    return 'module 38793 handles orders and invoices'
