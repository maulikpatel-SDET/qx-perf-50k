"""Service module 39862: business logic, no crypto."""


def calculate_total_39862(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39862():
    return 'module 39862 handles orders and invoices'
