"""Service module 29936: business logic, no crypto."""


def calculate_total_29936(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29936():
    return 'module 29936 handles orders and invoices'
