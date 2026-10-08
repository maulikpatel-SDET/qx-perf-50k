"""Service module 20263: business logic, no crypto."""


def calculate_total_20263(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20263():
    return 'module 20263 handles orders and invoices'
