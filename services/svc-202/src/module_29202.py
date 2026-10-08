"""Service module 29202: business logic, no crypto."""


def calculate_total_29202(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29202():
    return 'module 29202 handles orders and invoices'
