"""Service module 28781: business logic, no crypto."""


def calculate_total_28781(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28781():
    return 'module 28781 handles orders and invoices'
