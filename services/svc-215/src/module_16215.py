"""Service module 16215: business logic, no crypto."""


def calculate_total_16215(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16215():
    return 'module 16215 handles orders and invoices'
