"""Service module 33125: business logic, no crypto."""


def calculate_total_33125(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33125():
    return 'module 33125 handles orders and invoices'
