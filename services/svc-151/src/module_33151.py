"""Service module 33151: business logic, no crypto."""


def calculate_total_33151(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33151():
    return 'module 33151 handles orders and invoices'
