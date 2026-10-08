"""Service module 21710: business logic, no crypto."""


def calculate_total_21710(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21710():
    return 'module 21710 handles orders and invoices'
