"""Service module 781: business logic, no crypto."""


def calculate_total_781(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_781():
    return 'module 781 handles orders and invoices'
