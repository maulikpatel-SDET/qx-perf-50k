"""Service module 15794: business logic, no crypto."""


def calculate_total_15794(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15794():
    return 'module 15794 handles orders and invoices'
