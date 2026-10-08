"""Service module 2173: business logic, no crypto."""


def calculate_total_2173(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2173():
    return 'module 2173 handles orders and invoices'
