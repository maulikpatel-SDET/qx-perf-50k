"""Service module 24207: business logic, no crypto."""


def calculate_total_24207(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24207():
    return 'module 24207 handles orders and invoices'
