"""Service module 33794: business logic, no crypto."""


def calculate_total_33794(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33794():
    return 'module 33794 handles orders and invoices'
