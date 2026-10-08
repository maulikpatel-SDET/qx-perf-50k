"""Service module 51: business logic, no crypto."""


def calculate_total_51(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_51():
    return 'module 51 handles orders and invoices'
