"""Service module 19914: business logic, no crypto."""


def calculate_total_19914(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19914():
    return 'module 19914 handles orders and invoices'
