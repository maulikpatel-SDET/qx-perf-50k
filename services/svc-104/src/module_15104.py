"""Service module 15104: business logic, no crypto."""


def calculate_total_15104(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15104():
    return 'module 15104 handles orders and invoices'
