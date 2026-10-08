"""Service module 29151: business logic, no crypto."""


def calculate_total_29151(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29151():
    return 'module 29151 handles orders and invoices'
