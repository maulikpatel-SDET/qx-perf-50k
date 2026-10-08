"""Service module 1331: business logic, no crypto."""


def calculate_total_1331(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1331():
    return 'module 1331 handles orders and invoices'
