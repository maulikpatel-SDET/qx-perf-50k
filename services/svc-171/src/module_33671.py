"""Service module 33671: business logic, no crypto."""


def calculate_total_33671(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33671():
    return 'module 33671 handles orders and invoices'
