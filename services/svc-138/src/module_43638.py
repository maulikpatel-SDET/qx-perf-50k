"""Service module 43638: business logic, no crypto."""


def calculate_total_43638(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43638():
    return 'module 43638 handles orders and invoices'
