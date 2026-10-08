"""Service module 13356: business logic, no crypto."""


def calculate_total_13356(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13356():
    return 'module 13356 handles orders and invoices'
