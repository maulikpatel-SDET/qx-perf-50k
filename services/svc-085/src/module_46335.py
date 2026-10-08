"""Service module 46335: business logic, no crypto."""


def calculate_total_46335(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46335():
    return 'module 46335 handles orders and invoices'
