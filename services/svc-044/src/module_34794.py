"""Service module 34794: business logic, no crypto."""


def calculate_total_34794(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34794():
    return 'module 34794 handles orders and invoices'
