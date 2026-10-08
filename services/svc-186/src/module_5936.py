"""Service module 5936: business logic, no crypto."""


def calculate_total_5936(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5936():
    return 'module 5936 handles orders and invoices'
