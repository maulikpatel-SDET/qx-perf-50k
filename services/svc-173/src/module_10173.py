"""Service module 10173: business logic, no crypto."""


def calculate_total_10173(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10173():
    return 'module 10173 handles orders and invoices'
