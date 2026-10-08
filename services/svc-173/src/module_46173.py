"""Service module 46173: business logic, no crypto."""


def calculate_total_46173(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46173():
    return 'module 46173 handles orders and invoices'
