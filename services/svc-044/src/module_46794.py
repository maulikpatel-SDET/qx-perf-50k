"""Service module 46794: business logic, no crypto."""


def calculate_total_46794(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46794():
    return 'module 46794 handles orders and invoices'
