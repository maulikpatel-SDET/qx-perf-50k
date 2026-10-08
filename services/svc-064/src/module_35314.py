"""Service module 35314: business logic, no crypto."""


def calculate_total_35314(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35314():
    return 'module 35314 handles orders and invoices'
