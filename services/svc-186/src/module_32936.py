"""Service module 32936: business logic, no crypto."""


def calculate_total_32936(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32936():
    return 'module 32936 handles orders and invoices'
