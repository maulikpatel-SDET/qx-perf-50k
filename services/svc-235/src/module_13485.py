"""Service module 13485: business logic, no crypto."""


def calculate_total_13485(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13485():
    return 'module 13485 handles orders and invoices'
