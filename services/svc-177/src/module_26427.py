"""Service module 26427: business logic, no crypto."""


def calculate_total_26427(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26427():
    return 'module 26427 handles orders and invoices'
