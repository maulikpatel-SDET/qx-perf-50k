"""Service module 15972: business logic, no crypto."""


def calculate_total_15972(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15972():
    return 'module 15972 handles orders and invoices'
