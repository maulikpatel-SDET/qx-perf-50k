"""Service module 21226: business logic, no crypto."""


def calculate_total_21226(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21226():
    return 'module 21226 handles orders and invoices'
