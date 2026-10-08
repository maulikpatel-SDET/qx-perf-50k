"""Service module 46936: business logic, no crypto."""


def calculate_total_46936(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46936():
    return 'module 46936 handles orders and invoices'
