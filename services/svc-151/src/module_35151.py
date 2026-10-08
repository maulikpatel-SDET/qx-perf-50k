"""Service module 35151: business logic, no crypto."""


def calculate_total_35151(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35151():
    return 'module 35151 handles orders and invoices'
