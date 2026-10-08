"""Service module 8181: business logic, no crypto."""


def calculate_total_8181(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8181():
    return 'module 8181 handles orders and invoices'
