"""Service module 1252: business logic, no crypto."""


def calculate_total_1252(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1252():
    return 'module 1252 handles orders and invoices'
