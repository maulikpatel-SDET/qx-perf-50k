"""Service module 27638: business logic, no crypto."""


def calculate_total_27638(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27638():
    return 'module 27638 handles orders and invoices'
