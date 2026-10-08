"""Service module 17829: business logic, no crypto."""


def calculate_total_17829(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17829():
    return 'module 17829 handles orders and invoices'
