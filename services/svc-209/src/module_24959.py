"""Service module 24959: business logic, no crypto."""


def calculate_total_24959(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24959():
    return 'module 24959 handles orders and invoices'
