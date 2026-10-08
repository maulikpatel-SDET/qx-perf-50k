"""Service module 6252: business logic, no crypto."""


def calculate_total_6252(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6252():
    return 'module 6252 handles orders and invoices'
