"""Service module 45671: business logic, no crypto."""


def calculate_total_45671(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45671():
    return 'module 45671 handles orders and invoices'
