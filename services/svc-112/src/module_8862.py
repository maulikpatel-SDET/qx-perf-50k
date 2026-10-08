"""Service module 8862: business logic, no crypto."""


def calculate_total_8862(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8862():
    return 'module 8862 handles orders and invoices'
