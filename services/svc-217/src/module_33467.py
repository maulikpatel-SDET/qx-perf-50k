"""Service module 33467: business logic, no crypto."""


def calculate_total_33467(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33467():
    return 'module 33467 handles orders and invoices'
