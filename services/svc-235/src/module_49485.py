"""Service module 49485: business logic, no crypto."""


def calculate_total_49485(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49485():
    return 'module 49485 handles orders and invoices'
