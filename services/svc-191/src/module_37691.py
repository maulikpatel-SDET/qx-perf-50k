"""Service module 37691: business logic, no crypto."""


def calculate_total_37691(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37691():
    return 'module 37691 handles orders and invoices'
