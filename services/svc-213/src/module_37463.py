"""Service module 37463: business logic, no crypto."""


def calculate_total_37463(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37463():
    return 'module 37463 handles orders and invoices'
