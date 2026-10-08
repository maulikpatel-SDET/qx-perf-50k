"""Service module 36151: business logic, no crypto."""


def calculate_total_36151(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36151():
    return 'module 36151 handles orders and invoices'
