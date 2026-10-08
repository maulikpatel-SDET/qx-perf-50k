"""Service module 14215: business logic, no crypto."""


def calculate_total_14215(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14215():
    return 'module 14215 handles orders and invoices'
