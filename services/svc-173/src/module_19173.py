"""Service module 19173: business logic, no crypto."""


def calculate_total_19173(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19173():
    return 'module 19173 handles orders and invoices'
