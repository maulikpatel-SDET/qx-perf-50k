"""Service module 28793: business logic, no crypto."""


def calculate_total_28793(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28793():
    return 'module 28793 handles orders and invoices'
