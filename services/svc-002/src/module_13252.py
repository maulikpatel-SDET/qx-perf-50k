"""Service module 13252: business logic, no crypto."""


def calculate_total_13252(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13252():
    return 'module 13252 handles orders and invoices'
