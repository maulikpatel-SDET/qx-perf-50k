"""Service module 6485: business logic, no crypto."""


def calculate_total_6485(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6485():
    return 'module 6485 handles orders and invoices'
