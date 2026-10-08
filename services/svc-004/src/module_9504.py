"""Service module 9504: business logic, no crypto."""


def calculate_total_9504(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9504():
    return 'module 9504 handles orders and invoices'
