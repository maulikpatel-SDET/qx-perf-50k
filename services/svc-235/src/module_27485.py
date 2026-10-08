"""Service module 27485: business logic, no crypto."""


def calculate_total_27485(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27485():
    return 'module 27485 handles orders and invoices'
