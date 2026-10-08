"""Service module 27339: business logic, no crypto."""


def calculate_total_27339(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27339():
    return 'module 27339 handles orders and invoices'
