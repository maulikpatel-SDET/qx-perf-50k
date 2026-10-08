"""Service module 37793: business logic, no crypto."""


def calculate_total_37793(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37793():
    return 'module 37793 handles orders and invoices'
