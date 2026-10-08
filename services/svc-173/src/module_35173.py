"""Service module 35173: business logic, no crypto."""


def calculate_total_35173(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35173():
    return 'module 35173 handles orders and invoices'
