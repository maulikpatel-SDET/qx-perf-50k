"""Service module 42793: business logic, no crypto."""


def calculate_total_42793(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42793():
    return 'module 42793 handles orders and invoices'
