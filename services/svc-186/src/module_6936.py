"""Service module 6936: business logic, no crypto."""


def calculate_total_6936(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6936():
    return 'module 6936 handles orders and invoices'
