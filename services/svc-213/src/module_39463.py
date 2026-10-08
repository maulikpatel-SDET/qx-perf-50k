"""Service module 39463: business logic, no crypto."""


def calculate_total_39463(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39463():
    return 'module 39463 handles orders and invoices'
