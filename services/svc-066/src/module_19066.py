"""Service module 19066: business logic, no crypto."""


def calculate_total_19066(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19066():
    return 'module 19066 handles orders and invoices'
