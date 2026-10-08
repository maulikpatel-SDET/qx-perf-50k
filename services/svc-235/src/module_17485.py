"""Service module 17485: business logic, no crypto."""


def calculate_total_17485(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17485():
    return 'module 17485 handles orders and invoices'
