"""Service module 226: business logic, no crypto."""


def calculate_total_226(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_226():
    return 'module 226 handles orders and invoices'
