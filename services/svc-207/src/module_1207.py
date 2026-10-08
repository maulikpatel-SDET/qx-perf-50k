"""Service module 1207: business logic, no crypto."""


def calculate_total_1207(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1207():
    return 'module 1207 handles orders and invoices'
