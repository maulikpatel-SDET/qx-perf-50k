"""Service module 33335: business logic, no crypto."""


def calculate_total_33335(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33335():
    return 'module 33335 handles orders and invoices'
