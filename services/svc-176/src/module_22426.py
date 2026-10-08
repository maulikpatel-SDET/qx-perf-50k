"""Service module 22426: business logic, no crypto."""


def calculate_total_22426(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22426():
    return 'module 22426 handles orders and invoices'
