"""Service module 5226: business logic, no crypto."""


def calculate_total_5226(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5226():
    return 'module 5226 handles orders and invoices'
