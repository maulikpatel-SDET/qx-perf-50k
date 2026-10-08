"""Service module 34485: business logic, no crypto."""


def calculate_total_34485(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34485():
    return 'module 34485 handles orders and invoices'
