"""Service module 44272: business logic, no crypto."""


def calculate_total_44272(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44272():
    return 'module 44272 handles orders and invoices'
