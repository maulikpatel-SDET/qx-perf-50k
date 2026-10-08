"""Service module 46793: business logic, no crypto."""


def calculate_total_46793(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46793():
    return 'module 46793 handles orders and invoices'
