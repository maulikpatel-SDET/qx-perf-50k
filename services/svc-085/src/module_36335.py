"""Service module 36335: business logic, no crypto."""


def calculate_total_36335(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36335():
    return 'module 36335 handles orders and invoices'
