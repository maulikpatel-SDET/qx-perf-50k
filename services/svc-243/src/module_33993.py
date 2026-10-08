"""Service module 33993: business logic, no crypto."""


def calculate_total_33993(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33993():
    return 'module 33993 handles orders and invoices'
