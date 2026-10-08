"""Service module 33617: business logic, no crypto."""


def calculate_total_33617(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33617():
    return 'module 33617 handles orders and invoices'
