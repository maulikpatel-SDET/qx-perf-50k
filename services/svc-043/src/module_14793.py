"""Service module 14793: business logic, no crypto."""


def calculate_total_14793(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14793():
    return 'module 14793 handles orders and invoices'
