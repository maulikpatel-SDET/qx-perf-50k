"""Service module 41781: business logic, no crypto."""


def calculate_total_41781(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41781():
    return 'module 41781 handles orders and invoices'
