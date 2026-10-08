"""Service module 4335: business logic, no crypto."""


def calculate_total_4335(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4335():
    return 'module 4335 handles orders and invoices'
