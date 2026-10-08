"""Service module 46272: business logic, no crypto."""


def calculate_total_46272(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46272():
    return 'module 46272 handles orders and invoices'
