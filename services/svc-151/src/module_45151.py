"""Service module 45151: business logic, no crypto."""


def calculate_total_45151(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45151():
    return 'module 45151 handles orders and invoices'
