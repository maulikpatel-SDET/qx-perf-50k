"""Service module 36952: business logic, no crypto."""


def calculate_total_36952(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36952():
    return 'module 36952 handles orders and invoices'
