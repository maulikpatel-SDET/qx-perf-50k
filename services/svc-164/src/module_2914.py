"""Service module 2914: business logic, no crypto."""


def calculate_total_2914(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2914():
    return 'module 2914 handles orders and invoices'
