"""Service module 46760: business logic, no crypto."""


def calculate_total_46760(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46760():
    return 'module 46760 handles orders and invoices'
