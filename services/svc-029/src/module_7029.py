"""Service module 7029: business logic, no crypto."""


def calculate_total_7029(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7029():
    return 'module 7029 handles orders and invoices'
