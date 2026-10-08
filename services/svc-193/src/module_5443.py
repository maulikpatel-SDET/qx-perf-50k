"""Service module 5443: business logic, no crypto."""


def calculate_total_5443(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5443():
    return 'module 5443 handles orders and invoices'
