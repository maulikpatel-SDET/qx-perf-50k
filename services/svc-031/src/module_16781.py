"""Service module 16781: business logic, no crypto."""


def calculate_total_16781(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16781():
    return 'module 16781 handles orders and invoices'
