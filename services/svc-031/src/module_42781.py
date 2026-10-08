"""Service module 42781: business logic, no crypto."""


def calculate_total_42781(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42781():
    return 'module 42781 handles orders and invoices'
