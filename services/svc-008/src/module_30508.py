"""Service module 30508: business logic, no crypto."""


def calculate_total_30508(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30508():
    return 'module 30508 handles orders and invoices'
