"""Service module 23011: business logic, no crypto."""


def calculate_total_23011(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23011():
    return 'module 23011 handles orders and invoices'
