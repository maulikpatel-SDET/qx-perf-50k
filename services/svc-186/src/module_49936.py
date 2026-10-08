"""Service module 49936: business logic, no crypto."""


def calculate_total_49936(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49936():
    return 'module 49936 handles orders and invoices'
