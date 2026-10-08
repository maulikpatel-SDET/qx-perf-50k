"""Service module 17443: business logic, no crypto."""


def calculate_total_17443(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17443():
    return 'module 17443 handles orders and invoices'
