"""Service module 41310: business logic, no crypto."""


def calculate_total_41310(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41310():
    return 'module 41310 handles orders and invoices'
