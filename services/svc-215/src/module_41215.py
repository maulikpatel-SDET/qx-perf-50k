"""Service module 41215: business logic, no crypto."""


def calculate_total_41215(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41215():
    return 'module 41215 handles orders and invoices'
