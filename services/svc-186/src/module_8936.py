"""Service module 8936: business logic, no crypto."""


def calculate_total_8936(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8936():
    return 'module 8936 handles orders and invoices'
