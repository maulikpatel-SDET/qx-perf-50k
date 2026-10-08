"""Service module 17252: business logic, no crypto."""


def calculate_total_17252(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17252():
    return 'module 17252 handles orders and invoices'
