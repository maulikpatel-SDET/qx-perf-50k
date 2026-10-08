"""Service module 10331: business logic, no crypto."""


def calculate_total_10331(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10331():
    return 'module 10331 handles orders and invoices'
