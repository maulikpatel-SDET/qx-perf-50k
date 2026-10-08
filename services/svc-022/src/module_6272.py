"""Service module 6272: business logic, no crypto."""


def calculate_total_6272(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6272():
    return 'module 6272 handles orders and invoices'
