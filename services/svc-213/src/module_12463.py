"""Service module 12463: business logic, no crypto."""


def calculate_total_12463(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12463():
    return 'module 12463 handles orders and invoices'
