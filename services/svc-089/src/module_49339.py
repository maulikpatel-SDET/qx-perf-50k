"""Service module 49339: business logic, no crypto."""


def calculate_total_49339(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49339():
    return 'module 49339 handles orders and invoices'
