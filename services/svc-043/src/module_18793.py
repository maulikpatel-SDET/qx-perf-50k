"""Service module 18793: business logic, no crypto."""


def calculate_total_18793(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18793():
    return 'module 18793 handles orders and invoices'
