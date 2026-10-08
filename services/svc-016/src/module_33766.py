"""Service module 33766: business logic, no crypto."""


def calculate_total_33766(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33766():
    return 'module 33766 handles orders and invoices'
