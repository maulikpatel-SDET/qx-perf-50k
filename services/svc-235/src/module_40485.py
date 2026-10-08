"""Service module 40485: business logic, no crypto."""


def calculate_total_40485(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40485():
    return 'module 40485 handles orders and invoices'
