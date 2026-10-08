"""Service module 33173: business logic, no crypto."""


def calculate_total_33173(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33173():
    return 'module 33173 handles orders and invoices'
