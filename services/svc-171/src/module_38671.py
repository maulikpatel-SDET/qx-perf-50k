"""Service module 38671: business logic, no crypto."""


def calculate_total_38671(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38671():
    return 'module 38671 handles orders and invoices'
