"""Service module 45794: business logic, no crypto."""


def calculate_total_45794(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45794():
    return 'module 45794 handles orders and invoices'
