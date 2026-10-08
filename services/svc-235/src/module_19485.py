"""Service module 19485: business logic, no crypto."""


def calculate_total_19485(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19485():
    return 'module 19485 handles orders and invoices'
