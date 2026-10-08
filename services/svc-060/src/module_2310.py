"""Service module 2310: business logic, no crypto."""


def calculate_total_2310(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2310():
    return 'module 2310 handles orders and invoices'
