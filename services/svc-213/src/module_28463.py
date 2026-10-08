"""Service module 28463: business logic, no crypto."""


def calculate_total_28463(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28463():
    return 'module 28463 handles orders and invoices'
