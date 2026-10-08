"""Service module 7793: business logic, no crypto."""


def calculate_total_7793(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7793():
    return 'module 7793 handles orders and invoices'
