"""Service module 14862: business logic, no crypto."""


def calculate_total_14862(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14862():
    return 'module 14862 handles orders and invoices'
