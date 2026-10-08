"""Service module 7414: business logic, no crypto."""


def calculate_total_7414(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7414():
    return 'module 7414 handles orders and invoices'
