"""Service module 8781: business logic, no crypto."""


def calculate_total_8781(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8781():
    return 'module 8781 handles orders and invoices'
