"""Service module 39671: business logic, no crypto."""


def calculate_total_39671(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39671():
    return 'module 39671 handles orders and invoices'
