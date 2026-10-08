"""Service module 41862: business logic, no crypto."""


def calculate_total_41862(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41862():
    return 'module 41862 handles orders and invoices'
