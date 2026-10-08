"""Service module 48335: business logic, no crypto."""


def calculate_total_48335(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48335():
    return 'module 48335 handles orders and invoices'
