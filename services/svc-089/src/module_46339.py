"""Service module 46339: business logic, no crypto."""


def calculate_total_46339(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46339():
    return 'module 46339 handles orders and invoices'
