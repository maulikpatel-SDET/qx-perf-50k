"""Service module 11952: business logic, no crypto."""


def calculate_total_11952(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11952():
    return 'module 11952 handles orders and invoices'
