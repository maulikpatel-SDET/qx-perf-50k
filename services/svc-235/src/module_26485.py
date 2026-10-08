"""Service module 26485: business logic, no crypto."""


def calculate_total_26485(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26485():
    return 'module 26485 handles orders and invoices'
