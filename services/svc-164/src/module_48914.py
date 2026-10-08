"""Service module 48914: business logic, no crypto."""


def calculate_total_48914(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48914():
    return 'module 48914 handles orders and invoices'
