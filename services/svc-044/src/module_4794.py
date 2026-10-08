"""Service module 4794: business logic, no crypto."""


def calculate_total_4794(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4794():
    return 'module 4794 handles orders and invoices'
