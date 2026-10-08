"""Service module 35252: business logic, no crypto."""


def calculate_total_35252(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35252():
    return 'module 35252 handles orders and invoices'
