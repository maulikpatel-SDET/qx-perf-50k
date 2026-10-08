"""Service module 28936: business logic, no crypto."""


def calculate_total_28936(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28936():
    return 'module 28936 handles orders and invoices'
