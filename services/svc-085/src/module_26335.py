"""Service module 26335: business logic, no crypto."""


def calculate_total_26335(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26335():
    return 'module 26335 handles orders and invoices'
