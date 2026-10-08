"""Service module 27510: business logic, no crypto."""


def calculate_total_27510(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27510():
    return 'module 27510 handles orders and invoices'
