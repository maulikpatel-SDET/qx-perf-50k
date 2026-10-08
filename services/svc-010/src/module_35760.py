"""Service module 35760: business logic, no crypto."""


def calculate_total_35760(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35760():
    return 'module 35760 handles orders and invoices'
