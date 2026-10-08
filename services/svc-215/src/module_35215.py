"""Service module 35215: business logic, no crypto."""


def calculate_total_35215(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35215():
    return 'module 35215 handles orders and invoices'
