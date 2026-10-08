"""Service module 46012: business logic, no crypto."""


def calculate_total_46012(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46012():
    return 'module 46012 handles orders and invoices'
