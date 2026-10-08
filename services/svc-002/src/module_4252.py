"""Service module 4252: business logic, no crypto."""


def calculate_total_4252(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4252():
    return 'module 4252 handles orders and invoices'
