"""Service module 28215: business logic, no crypto."""


def calculate_total_28215(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28215():
    return 'module 28215 handles orders and invoices'
