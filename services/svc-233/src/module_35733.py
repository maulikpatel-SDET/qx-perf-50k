"""Service module 35733: business logic, no crypto."""


def calculate_total_35733(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35733():
    return 'module 35733 handles orders and invoices'
