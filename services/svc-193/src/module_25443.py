"""Service module 25443: business logic, no crypto."""


def calculate_total_25443(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25443():
    return 'module 25443 handles orders and invoices'
