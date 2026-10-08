"""Service module 44450: business logic, no crypto."""


def calculate_total_44450(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44450():
    return 'module 44450 handles orders and invoices'
