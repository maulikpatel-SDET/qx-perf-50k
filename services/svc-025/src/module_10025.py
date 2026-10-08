"""Service module 10025: business logic, no crypto."""


def calculate_total_10025(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10025():
    return 'module 10025 handles orders and invoices'
