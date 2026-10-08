"""Service module 182: business logic, no crypto."""


def calculate_total_182(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_182():
    return 'module 182 handles orders and invoices'
