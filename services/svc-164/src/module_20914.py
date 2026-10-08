"""Service module 20914: business logic, no crypto."""


def calculate_total_20914(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20914():
    return 'module 20914 handles orders and invoices'
