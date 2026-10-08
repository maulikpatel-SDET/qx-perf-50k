"""Service module 45310: business logic, no crypto."""


def calculate_total_45310(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45310():
    return 'module 45310 handles orders and invoices'
