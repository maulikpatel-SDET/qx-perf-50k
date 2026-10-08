"""Service module 12104: business logic, no crypto."""


def calculate_total_12104(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12104():
    return 'module 12104 handles orders and invoices'
