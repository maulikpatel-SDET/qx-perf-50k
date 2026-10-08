"""Service module 4638: business logic, no crypto."""


def calculate_total_4638(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4638():
    return 'module 4638 handles orders and invoices'
