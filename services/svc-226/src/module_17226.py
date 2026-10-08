"""Service module 17226: business logic, no crypto."""


def calculate_total_17226(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17226():
    return 'module 17226 handles orders and invoices'
