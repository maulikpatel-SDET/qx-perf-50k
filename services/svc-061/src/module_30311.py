"""Service module 30311: business logic, no crypto."""


def calculate_total_30311(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30311():
    return 'module 30311 handles orders and invoices'
