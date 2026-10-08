"""Service module 25862: business logic, no crypto."""


def calculate_total_25862(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25862():
    return 'module 25862 handles orders and invoices'
