"""Service module 39776: business logic, no crypto."""


def calculate_total_39776(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39776():
    return 'module 39776 handles orders and invoices'
